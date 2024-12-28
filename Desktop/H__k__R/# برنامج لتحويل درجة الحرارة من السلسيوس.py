
print(f"درجة الحرارة بالفهرنهايت: {fahrenheit}°F")
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>نموذج الدخول</title>
</head>
<body>
    <h2>أدخل بياناتك</h2>
    <form id="userForm">
        <label for="name">الاسم:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">البريد الإلكتروني:</label>
        <input type="email" id="email" name="email" required><br><br>

        <input type="submit" value="إرسال">
    </form>

    <h3>معلومات المدخلات:</h3>
    <div id="output"></div>

    <script src="script.js"></script>
</body>
</html>
