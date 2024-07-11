const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');
const mysql = require('mysql');
const path = require('path');
const dotenv = require('dotenv');
const session = require('express-session');
const crypto = require('crypto');

const app = express();
const port = process.env.PORT || 3001;

// 使用 dotenv 加載環境變量
dotenv.config({ path: path.join(__dirname, '.env') });

// 檢查環境變量
console.log('GMAIL_USER:', process.env.GMAIL_USER);
console.log('GMAIL_PASS:', process.env.GMAIL_PASS);

// 創建 MySQL 連接
let db = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_DATABASE
});

// 連接到 MySQL
function handleDisconnect() {
  db.connect((err) => {
    if (err) {
      console.error('資料庫連接失敗: ', err);
      setTimeout(handleDisconnect, 2000); // 2秒後重試連接
    } else {
      console.log('資料庫連接成功');
    }
  });

  db.on('error', (err) => {
    console.error('資料庫錯誤: ', err);
    if (err.code === 'PROTOCOL_CONNECTION_LOST' || err.code === 'ECONNREFUSED' || err.code === 'ER_ACCESS_DENIED_ERROR') {
      handleDisconnect(); // 自動重新連接
    } else {
      throw err;
    }
  });
}

handleDisconnect();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// 設置會話中間件
app.use(session({
  secret: 'your_secret_key', // 替換為你的密鑰
  resave: false,
  saveUninitialized: true,
  cookie: { maxAge: 60000 }
}));

// 創建 Nodemailer 傳輸
const transporter = nodemailer.createTransport({
  host: 'smtp.gmail.com',
  port: 465,
  secure: true,
  auth: {
    user: process.env.GMAIL_USER,
    pass: process.env.GMAIL_PASS
  }
});

// 設置靜態文件目錄
app.use(express.static(path.join(__dirname, 'public')));

// 路由處理
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

// 歡迎訊息路由
app.get('/', (req, res) => {
  res.send('歡迎來到用戶註冊系統。');
});

// 顯示資料庫內容的路由
app.get('/show-database', (req, res) => {
  const query = 'SELECT * FROM user'; // 假設你有一個叫 'user' 的表
  db.query(query, (err, results) => {
    if (err) {
      console.error('查詢失敗: ', err);
      return res.status(500).send('查詢資料庫失敗');
    }

    // 顯示查詢結果
    res.send(`
      <h1>資料庫內容</h1>
      <pre>${JSON.stringify(results, null, 2)}</pre>
    `);
  });
});

// 忘記密碼請求路由
app.post('/forgot-password', (req, res) => {
  const { email } = req.body;
  
  // 查找用戶
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

    // 臨時存儲令牌
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

// 重設密碼路由
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

    // 刪除臨時存儲的令牌
    delete app.locals[email];

    res.json({ success: true, message: '密碼重設成功。' });
  });
});

// 發送驗證碼的路由
app.post('/send-verification', (req, res) => {
  const { email } = req.body;
  const verificationCode = Math.floor(100000 + Math.random() * 900000).toString();
  const verificationCodeExpiry = new Date(Date.now() + 5 * 60 * 1000); // 設置驗證碼到期時間為5分鐘後

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

    // 臨時存儲驗證碼和到期時間
    app.locals[email] = {
      verificationCode,
      expiryTime: verificationCodeExpiry
    };

    res.json({ success: true });
  });
});

// 註冊用戶路由
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

  // 檢查是否有重複的 email 或 phone
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

      // 註冊成功後刪除臨時存儲的驗證碼數據
      delete app.locals[email];

      // 使用 res.json 返回成功訊息和重定向 URL
      res.json({ success: true, redirect: '/登入.html' });
    });
  });
});

// 登入用戶路由
app.post('/login', (req, res) => {
  const { email, password, rememberMe } = req.body;

  const loginUserQuery = `SELECT * FROM user WHERE email = ? AND password = ?`;
  db.query(loginUserQuery, [email, password], (err, results) => {
    if (err) {
      console.error('查詢失敗: ', err);
      return res.status(500).json({ success: false, message: '登入失敗，請重試。' });
    }

    if (results.length === 0) {
      return res.status(400).json({ success: false, message: '電子郵件或密碼錯誤。' });
    }

    // 假設登入成功，將用戶資料存入會話
    req.session.user = results[0];

    res.json({ success: true, redirect: '/儀錶板.html' });
  });
});

// 個人資訊路由
app.get('/個人資訊', (req, res) => {
  if (!req.session.user) {
    return res.status(401).json({ success: false, message: '未登入' });
  }

  res.json({ success: true, user: req.session.user });
});

// 登出用戶路由
app.post('/logout', (req, res) => {
  req.session.destroy((err) => {
    if (err) {
      return res.status(500).json({ success: false, message: '登出失敗' });
    }
    res.json({ success: true, message: '已成功登出' });
  });
});

// 啟動伺服器
app.listen(port, () => {
  console.log(`伺服器正在 http://localhost:${port} 運行`);
});
