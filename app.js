const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');
const bcrypt = require('bcrypt');

const app = express();
const port = 3000;

app.use(bodyParser.json());

// MySQL 連接
const db = mysql.createConnection({
    host: '140.131.114.242',
    user: 'ntub113209',
    password: 'Sw@23110565',
    database: '113-ntub113209'
});

// 連接到 MySQL
db.connect((err) => {
    if (err) {
        console.error('無法連接到資料庫:', err);
        return;
    }
    console.log('已連接到 MySQL 資料庫');
});

// 處理註冊請求
app.post('/register', (req, res) => {
    const { username, password, phone } = req.body;

    // 加密密碼
    bcrypt.hash(password, 10, (err, hashedPassword) => {
        if (err) {
            console.error('Unable to hash password:', err);
            return res.status(500).json({ success: false, message: 'Registration failed' });
        }

        // 插入用戶到資料庫
        const insertQuery = 'INSERT INTO users (username, password, phone) VALUES (?, ?, ?)';
        db.query(insertQuery, [username, hashedPassword, phone], (err, result) => {
            if (err) {
                console.error('Unable to insert user into database:', err);
                return res.status(500).json({ success: false, message: 'Registration failed' });
            }
            res.json({ success: true, message: 'Registration successful' });
        });
    });
});

// 啟動伺服器
app.listen(port, () => {
    console.log(`伺服器正在 http://localhost:${port} 運行`);
});
