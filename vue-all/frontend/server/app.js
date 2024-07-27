// // const express = require('express');
// // const mysql = require('mysql');
// // const nodemailer = require('nodemailer');
// // const dotenv = require('dotenv');

// // dotenv.config();

// // const app = express();
// // const port = 3000;


// // const db = mysql.createConnection({
// //   host: '140.131.114.242',        
// //   user: 'ntub113209',             
// //   password: 'Sw@23110565',        
// //   database: '113-ntub113209'      
// // });


// // db.connect((err) => {
// //   if (err) {
// //     console.error('無法連接到資料庫:', err);
// //     return;
// //   }
// //   console.log('已連接到 MySQL 資料庫');
// // });


// // app.use(express.json());


// // const transporter = nodemailer.createTransport({
// //   service: 'gmail',
// //   auth: {
// //     user: process.env.GMAIL_USER,
// //     pass: process.env.GMAIL_PASS
// //   }
// // });


// // app.get('/', (req, res) => {
// //   res.send('Hello, World!');
// // });


// app.post('/register', (req, res) => {
//   const { username, email, password, phone, verification_code } = req.body;


//   if (!username || !email || !password || !phone || !verification_code) {
//     return res.status(400).json({ success: false, message: '請填寫所有必填字段。' });
//   }


//   checkEmailExists(email, (exists) => {
//     if (exists) {
//       return res.status(400).json({ success: false, message: '此電子郵件已被註冊。' });
//     }

//     verifyCode(email, verification_code, (valid) => {
//       if (!valid) {
//         return res.status(400).json({ success: false, message: '驗證碼無效或已過期。' });
//       }


//       const query = 'INSERT INTO user (username, email, password, phone) VALUES (?, ?, ?, ?)';
//       db.query(query, [username, email, password, phone], (err, results) => {
//         if (err) {
//           return res.status(500).json({ success: false, message: '註冊失敗。' });
//         }
//         res.json({ success: true, message: '註冊成功。' });
//       });
//     });
//   });
// });


// function checkEmailExists(email, callback) {
//   const query = 'SELECT * FROM user WHERE email = ?';
//   db.query(query, [email], (err, results) => {
//     if (err) {
//       console.error('查詢錯誤:', err);
//       return callback(false);
//     }
//     callback(results.length > 0);
//   });
// }


// app.post('/send-verification', (req, res) => {
//   const { email } = req.body;


//   if (!validateEmail(email)) {
//     return res.status(400).json({ success: false, message: '請輸入有效的電子郵件地址。' });
//   }


//   const verification_code = generateVerificationCode();
//   const mailOptions = {
//     from: process.env.GMAIL_USER,
//     to: email,
//     subject: '您的驗證碼',
//     text: `您的驗證碼是 ${verification_code}，有效期限為5分鐘。`
//   };


//   saveVerificationCode(email, verification_code);

//   if (email === '11236035@ntub.edu.tw') {
//     transporter.sendMail(mailOptions, (err, info) => {
//       if (err) {
//         console.error('發送驗證碼失敗:', err);
//         return res.status(500).json({ success: false, message: '發送驗證碼失敗，請重試。' });
//       }
//       res.json({ success: true, message: '驗證碼已發送到您的電子郵件。' });
//     });
//   } else {
//     res.json({ success: true, message: '驗證碼已發送到您的電子郵件。' });
//   }
// });

// app.post('/verify-code', (req, res) => {
//   const { email, verification_code } = req.body;

//   verifyCode(email, verification_code, (valid) => {
//     if (!valid) {
//       return res.status(400).json({ success: false, message: '驗證碼無效或已過期。' });
//     }
//     res.json({ success: true, message: '驗證碼有效。' });
//   });
// });


// function saveVerificationCode(email, verification_code) {
//   const timestamp = new Date().getTime();
//   const query = 'INSERT INTO verification_codes (email, code, timestamp) VALUES (?, ?, ?) ON DUPLICATE KEY UPDATE code = VALUES(code), timestamp = VALUES(timestamp)';
//   db.query(query, [email, verification_code, timestamp], (err, results) => {
//     if (err) {
//       console.error('儲存驗證碼失敗:', err);
//     }
//   });
// }


// function verifyCode(email, verification_code, callback) {
//   const query = 'SELECT * FROM verification_codes WHERE email = ? AND code = ?';
//   db.query(query, [email, verification_code], (err, results) => {
//     if (err) {
//       console.error('查詢錯誤:', err);
//       return callback(false);
//     }
//     if (results.length === 0) {
//       return callback(false);
//     }

//     const { timestamp } = results[0];
//     const now = new Date().getTime();
//     if (now - timestamp > 5 * 60 * 1000) {
//       return callback(false);
//     }
//     callback(true);
//   });
// }


// function validateEmail(email) {
//   const re = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
//   return re.test(String(email).toLowerCase());
// }


// function generateVerificationCode() {
//   return Math.floor(100000 + Math.random() * 900000).toString();
// }

// app.listen(port, () => {
//   console.log(`伺服器運行在 http://localhost:${port}`);
// });
