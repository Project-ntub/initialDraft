function getVerificationCode() {
    const email = document.getElementById("email").value.trim();
    if (!validateEmail(email)) {
        alert("請輸入有效的電子郵件地址。");
        return;
    }

    fetch(`/frontend/send_verification_code/?email=${encodeURIComponent(email)}`)
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                alert("驗證碼已成功發送到您的電子郵件。");
                document.getElementById("verification-feedback").innerText =
                    "驗證碼已發送到您的電子郵件，有效期限5分鐘。";
            } else {
                alert("發送驗證碼失敗，請稍後再試。");
                document.getElementById("verification-feedback").innerText =
                    "發送驗證碼失敗，請稍後再試。";
            }
        })
        .catch((error) => {
            alert("發送驗證碼失敗，請稍後再試。");
            document.getElementById("verification-feedback").innerText =
                "發送驗證碼失敗，請稍後再試。";
        });
}

function validateEmail(email) {
    const re = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    return re.test(String(email).toLowerCase());
}
