<html>
<head>
    <title>Restricted</title>
</head>
<body>
    <h1>Restricted</h1>
%if name:
    <p>Hello {{name}} from {{ip}}. Welcome back.</p>
%else:
    <p>You are not logged in. Access denied.</p><a href="/login">Login</a></p>
</body>
</html>



