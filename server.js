const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');
const mysql = require('mysql');
const path = require('path');
const dotenv = require('dotenv');
const session = require('express-session');
const crypto = require('crypto');
const cors = require('cors');

const app = express();
const port = process.env.PORT || 3001;

dotenv.config({ path: path.join(__dirname, '.env') });

console.log('GMAIL_USER:', process.env.GMAIL_USER);
console.log('GMAIL_PASS:', process.env.GMAIL_PASS);

let db = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_DATABASE
});

function handleDisconnect() {
  db.connect((err) => {
    if (err) {
      console.error('資料庫連接失敗: ', err);
      setTimeout(handleDisconnect, 2000);
    } else {
      console.log('資料庫連接成功');
    }
  });

  db.on('error', (err) => {
    console.error('資料庫錯誤: ', err);
    if (err.code === 'PROTOCOL_CONNECTION_LOST' || err.code === 'ECONNREFUSED' || err.code === 'ER_ACCESS_DENIED_ERROR') {
      handleDisconnect();
    } else {
      throw err;
    }
  });
}

handleDisconnect();

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.use(session({
  secret: 'your_secret_key',
  resave: false,
  saveUninitialized: true,
  cookie: { maxAge: 600000 }
}));

const transporter = nodemailer.createTransport({
  host: 'smtp.gmail.com',
  port: 465,
  secure: true,
  auth: {
    user: process.env.GMAIL_USER,
    pass: process.env.GMAIL_PASS
  }
});

app.use(express.static(path.join(__dirname, 'public')));

app.use((req, res, next) => {
  if (req.session.user) {
    const logActionQuery = `INSERT INTO user_history (user_id, action) VALUES (?, ?)`;
    const action = req.method + ' ' + req.url;
    db.query(logActionQuery, [req.session.user.id, action], (logErr) => {
      if (logErr) {
        console.error('記錄行為失敗:', logErr);
      }
    });
  }
  next();
});

app.get('/登入.html', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', '登入.html'));
});

app.get('/註冊.html', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', '註冊.html'));
});

app.get('/儀錶板.html', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', '儀錶板.html'));
});

app.get('/重設密碼.html', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', '重設密碼.html'));
});

app.get('/', (req, res) => {
  res.send('歡迎來到用戶註冊系統。');
});

app.get('/show-database', (req, res) => {
  const query = 'SELECT * FROM user';
  db.query(query, (err, results) => {
    if (err) {
      console.error('查詢失敗: ', err);
      return res.status(500).send('查詢資料庫失敗');
    }

    res.send(`
      <h1>資料庫內容</h1>
      <pre>${JSON.stringify(results, null, 2)}</pre>
    `);
  });
});

app.get('/api/user-data', (req, res) => {
  if (!req.session.user) {
    return res.status(401).json({ success: false, message: '未登入' });
  }

  const query = 'SELECT * FROM user WHERE id = ?';
  db.query(query, [req.session.user.id], (err, results) => {
    if (err) {
      console.error('查詢失敗: ', err);
      return res.status(500).json({ success: false, message: '查詢失敗' });
    }

    res.json({ success: true, data: results });
  });
});

app.post('/forgot-password', (req, res) => {
  const { email } = req.body;

  const findUserQuery = `SELECT * FROM user WHERE email = ?`;
  db.query(findUserQuery, [email], (err, results) => {
    if (err) {
      console.error('查詢失敗: ', err);
      return res.status(500).json({ success: false, message: '查詢失敗，請重試。' });
    }

    if (results.length === 0) {
      return res.status(404).json({ success: false, message: '未找到該郵箱對應的用戶。' });
    }

    const user = results[0];
    const resetToken = crypto.randomBytes(20).toString('hex');
    const resetUrl = `http://localhost:${port}/重設密碼.html?email=${encodeURIComponent(email)}&token=${encodeURIComponent(resetToken)}`;

    app.locals[email] = resetToken;

    const mailOptions = {
      from: process.env.GMAIL_USER,
      to: email,
      subject: '重設密碼請求',
      html: `請點擊以下鏈接來重設您的密碼：<br><br><a href="${resetUrl}">${resetUrl}</a>`
    };

    transporter.sendMail(mailOptions, (error, info) => {
      if (error) {
        console.error('郵件發送失敗: ', error);
        return res.status(500).json({ success: false, message: '發送重設鏈接失敗，請重試。' });
      }
      console.log('郵件發送成功: ', info.response);
      res.json({ success: true, message: '重設鏈接已發送到您的郵箱。' });
    });
  });
});

app.post('/reset-password', (req, res) => {
  const { email, token, newPassword } = req.body;

  if (app.locals[email] !== token) {
    return res.status(400).json({ success: false, message: '無效的重設令牌。' });
  }

  const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
  if (!passwordRegex.test(newPassword)) {
    return res.status(400).json({ success: false, message: '密碼必須包含至少8個字符，且包括大小寫字母、數字和特殊字符。' });
  }

  const updatePasswordQuery = `UPDATE user SET password = ? WHERE email = ?`;
  db.query(updatePasswordQuery, [newPassword, email], (err, result) => {
    if (err) {
      console.error('更新密碼失敗: ', err);
      return res.status(500).json({ success: false, message: '重設密碼失敗，請重試。' });
    }

    delete app.locals[email];

    res.json({ success: true, message: '密碼重設成功。' });
  });
});

app.post('/send-verification', (req, res) => {
  const { email } = req.body;
  const verificationCode = Math.floor(100000 + Math.random() * 900000).toString();
  const verificationCodeExpiry = new Date(Date.now() + 5 * 60 * 1000);

  console.log(`生成的驗證碼: ${verificationCode}，到期時間: ${verificationCodeExpiry}`);

  const mailOptions = {
    from: process.env.GMAIL_USER,
    to: email,
    subject: '驗證碼',
    text: `您的驗證碼是：${verificationCode}`
  };

  transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
      console.error('郵件發送失敗: ', error);
      return res.status(500).json({ success: false, message: '發送驗證碼失敗，請重試。' });
    }
    console.log('郵件發送成功: ', info.response);

    app.locals[email] = {
      verificationCode,
      expiryTime: verificationCodeExpiry
    };

    res.json({ success: true });
  });
});

app.post('/register', (req, res) => {
  const { username, email, password, phone, inputCode } = req.body;

  const storedData = app.locals[email];
  if (!storedData) {
    return res.status(400).json({ success: false, message: '驗證碼未發送，請先獲取驗證碼。' });
  }

  const { verificationCode, expiryTime } = storedData;

  if (inputCode !== verificationCode) {
    return res.status(400).json({ success: false, message: '驗證碼錯誤。' });
  }

  if (new Date() > new Date(expiryTime)) {
    return res.status(400).json({ success: false, message: '驗證碼已過期。' });
  }

  const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
  if (!passwordRegex.test(password)) {
    return res.status(400).json({ success: false, message: '密碼必須包含至少8個字符，且包括大小寫字母、數字和特殊字符。' });
  }

  const checkDuplicateQuery = `SELECT * FROM user WHERE email = ? OR phone = ?`;
  db.query(checkDuplicateQuery, [email, phone], (err, results) => {
    if (err) {
      console.error('查詢失敗: ', err);
      return res.status(500).json({ success: false, message: '註冊失敗，請重試。' });
    }

    if (results.length > 0) {
      return res.status(400).json({ success: false, message: '電子郵件或電話號碼已被使用。' });
    }

    const insertUserQuery = `INSERT INTO user (username, email, password, phone, is_verified, is_superuser, is_approved, last_login, date_joined) 
                             VALUES (?, ?, ?, ?, 1, 0, 0, NOW(), NOW())`;
    db.query(insertUserQuery, [username, email, password, phone], (err, result) => {
      if (err) {
        console.error('資料庫錯誤: ', err);
        return res.status(500).json({ success: false, message: '註冊失敗，請重試。' });
      }

      delete app.locals[email];

      res.json({ success: true, redirect: '/登入.html' });
    });
  });
});

app.post('/login', (req, res) => {
  const { email, password, otp } = req.body;

  const loginUserQuery = `SELECT * FROM user WHERE email = ?`;
  db.query(loginUserQuery, [email], (err, results) => {
    if (err) {
      console.error('查詢失敗: ', err);
      return res.status(500).json({ success: false, message: '登入失敗，請重試。' });
    }

    if (results.length === 0) {
      console.log('用戶不存在或密碼錯誤');
      return res.status(400).json({ success: false, message: '電子郵件或密碼錯誤。' });
    }

    const user = results[0];

    if (user.password !== password) {
      console.log('用戶不存在或密碼錯誤');
      return res.status(400).json({ success: false, message: '電子郵件或密碼錯誤。' });
    }

    const storedOTP = app.locals[email] && app.locals[email].otp;
    if (storedOTP !== otp) {
      console.log('OTP錯誤');
      return res.status(400).json({ success: false, message: 'OTP錯誤。' });
    }

    console.log('用戶登入成功', user);

    req.session.user = user;

    const logActionQuery = `INSERT INTO user_history (user_id, action) VALUES (?, '登入')`;
    db.query(logActionQuery, [user.id], (logErr) => {
      if (logErr) {
        console.error('記錄行為失敗:', logErr);
      }
    });

    res.json({ success: true, redirect: '/儀錶板.html' });
  });
});

app.get('/個人資訊', (req, res) => {
  if (!req.session.user) {
    return res.status(401).json({ success: false, message: '未登入' });
  }

  res.json({ success: true, user: req.session.user });
});

app.post('/logout', (req, res) => {
  if (req.session.user) {
    const logActionQuery = `INSERT INTO user_history (user_id, action) VALUES (?, '登出')`;
    db.query(logActionQuery, [req.session.user.id], (logErr) => {
      if (logErr) {
        console.error('記錄行為失敗:', logErr);
      }
    });
  }

  req.session.destroy((err) => {
    if (err) {
      return res.status(500).json({ success: false, message: '登出失敗' });
    }
    res.json({ success: true, message: '已成功登出' });
  });
});

app.post('/change-password', (req, res) => {
  const { currentPassword, newPassword } = req.body;
  const userId = req.session.user.id;

  const getUserQuery = `SELECT * FROM user WHERE id = ?`;
  db.query(getUserQuery, [userId], (err, results) => {
    if (err) {
      console.error('查詢失敗: ', err);
      return res.status(500).json({ success: false, message: '查詢失敗，請重試。' });
    }

    const user = results[0];
    if (user.password !== currentPassword) {
      return res.status(400).json({ success: false, message: '原密碼不正確' });
    }

    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    if (!passwordRegex.test(newPassword)) {
      return res.status(400).json({ success: false, message: '新密碼不符合要求' });
    }

    const updatePasswordQuery = `UPDATE user SET password = ? WHERE id = ?`;
    db.query(updatePasswordQuery, [newPassword, userId], (err, result) => {
      if (err) {
        console.error('更新密碼失敗: ', err);
        return res.status(500).json({ success: false, message: '更新密碼失敗，請重試。' });
      }

      const logActionQuery = `INSERT INTO user_history (user_id, action) VALUES (?, '更改密碼')`;
      db.query(logActionQuery, [userId], (logErr) => {
        if (logErr) {
          console.error('記錄行為失敗:', logErr);
        }
      });

      res.json({ success: true, message: '密碼更改成功' });
    });
  });
});

app.post('/update-preferences', (req, res) => {
  if (!req.session.user) {
    return res.status(401).json({ success: false, message: '未登入' });
  }

  const { fontSize, notification, autoLogin, authentication } = req.body;
  const userId = req.session.user.id;

  const notificationsEnabled = notification === 'enable' ? 1 : 0;
  const autoLoginEnabled = autoLogin === 'enable' ? 1 : 0;
  const authenticationEnabled = authentication === 'enable' ? 1 : 0;

  const updatePreferencesQuery = `UPDATE user SET font_size = ?, notifications_enabled = ?, auto_login_enabled = ?, authentication_enabled = ? WHERE id = ?`;
  db.query(updatePreferencesQuery, [fontSize, notificationsEnabled, autoLoginEnabled, authenticationEnabled, userId], (err, result) => {
    if (err) {
      console.error('更新偏好設定失敗: ', err);
      return res.status(500).json({ success: false, message: '更新偏好設定失敗，請重試。' });
    }

    const logActionQuery = `INSERT INTO user_history (user_id, action) VALUES (?, '更新偏好設定')`;
    db.query(logActionQuery, [userId], (logErr) => {
      if (logErr) {
        console.error('記錄行為失敗:', logErr);
      }
    });

    if (notification === 'enable') {
      const mailOptions = {
        from: process.env.GMAIL_USER,
        to: req.session.user.email,
        subject: '通知已開啟',
        text: '您已成功開啟通知。'
      };

      transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
          console.error('郵件發送失敗:', error);
          return res.status(500).json({ success: false, message: '發送通知郵件失敗，請重試。' });
        }
        console.log('郵件發送成功:', info.response);
      });
    }

    res.json({ success: true, message: '偏好設定更新成功' });
  });
});

app.post('/update-profile', (req, res) => {
  if (!req.session.user) {
    return res.status(401).json({ success: false, message: '未登入' });
  }

  const { name, department, position, phone, email } = req.body;
  const userId = req.session.user.id;

  const updateProfileQuery = `UPDATE user SET username = ?, department_id = ?, position_id = ?, phone = ?, email = ? WHERE id = ?`;
  db.query(updateProfileQuery, [name, department, position, phone, email, userId], (err, result) => {
    if (err) {
      console.error('更新資料失敗: ', err);
      return res.status(500).json({ success: false, message: '更新資料失敗，請重試。' });
    }

    const logActionQuery = `INSERT INTO user_history (user_id, action) VALUES (?, '更新個人資料')`;
    db.query(logActionQuery, [userId], (logErr) => {
      if (logErr) {
        console.error('記錄行為失敗:', logErr);
      }
    });

    res.json({ success: true, message: '資料更新成功' });
  });
});

// 新增發送 OTP 的路由
app.post('/send-otp', (req, res) => {
  const { email } = req.body;
  const otp = Math.floor(100000 + Math.random() * 900000).toString();
  app.locals[email] = { otp, expiry: Date.now() + 300000 }; // OTP 五分鐘內有效

  const mailOptions = {
    from: process.env.GMAIL_USER,
    to: email,
    subject: '您的 OTP',
    text: `您的 OTP 是：${otp}`
  };

  transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
      console.error('郵件發送失敗:', error);
      return res.status(500).json({ success: false, message: '發送 OTP 失敗，請重試。' });
    }
    console.log('郵件發送成功:', info.response);
    res.json({ success: true, message: 'OTP 已發送到您的郵箱。' });
  });
});

// 歷史紀錄 API
app.get('/api/history', (req, res) => {
  if (!req.session.user) {
    return res.json([{ action: '尚未登入，目前無紀錄' }]);
  }

  const historyQuery = `SELECT action, timestamp FROM user_history WHERE user_id = ? ORDER BY timestamp DESC`;
  db.query(historyQuery, [req.session.user.id], (err, results) => {
    if (err) {
      console.error('查詢歷史紀錄失敗: ', err);
      return res.status(500).json({ success: false, message: '查詢歷史紀錄失敗' });
    }

    res.json(results);
  });
});

app.listen(port, () => {
  console.log(`伺服器正在 http://localhost:${port} 運行`);
});
