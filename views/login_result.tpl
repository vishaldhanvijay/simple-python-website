<html>
<head>
    <title>Login result</title>
</head>
<body>
    <h1>Login result</h1>
%if username:
    <p>Welcome {{name}}! You are now logged in.</p>
    <p>Please proceed to the <a href="/restricted">RESTRICTED AREA</a>.</p>
%else:
    <p>Login failed. Access denied.</p>
    <p><a href="/login">Login</a></p>
</body>
</html>
