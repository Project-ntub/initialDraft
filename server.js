const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');
const mysql = require('mysql');
const path = require('path');
const dotenv = require('dotenv');

const app = express();
const port = process.env.PORT || 3001;

// 使用 dotenv 加載環境變量
dotenv.config({ path: path.join(__dirname, '.env') });

// 檢查環境變量
console.log('GMAIL_USER:', process.env.GMAIL_USER);
console.log('GMAIL_PASS:', process.env.GMAIL_PASS);

// 創建 MySQL 連接
const db = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_DATABASE
});

db.connect((err) => {
  if (err) {
    console.error('資料庫連接失敗: ', err);
    throw err;
  }
  console.log('資料庫連接成功');
});

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

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

  const insertUserQuery = 'INSERT INTO user (username, email, password, phone, is_verified) VALUES (?, ?, ?, ?, 1)';
  db.query(insertUserQuery, [username, email, password, phone], (err, result) => {
    if (err) {
      console.error('資料庫錯誤: ', err);
      return res.status(500).json({ success: false, message: '註冊失敗，請重試。' });
    }

    // 註冊成功後刪除臨時存儲的驗證碼數據
    delete app.locals[email];

    // 使用 res.redirect 重定向到登錄頁面
    res.json({ success: true, redirect: '/login.html' });
  });
});

// 啟動伺服器
app.listen(port, () => {
  console.log(`伺服器正在 http://localhost:${port} 運行`);
});
