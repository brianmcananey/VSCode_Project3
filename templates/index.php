<?php

// Show all errors
error_reporting(E_ALL);
ini_set('display_errors', 1);

session_start();

if (isset($_SESSION["user_id"])) {
    
    $mysqli = require __DIR__ . "templates\database.php";

    $sql = "SELECT * FROM user
            WHERE id = {$_SESSION["user_id"]}";

    $result = $mysqli->query($sql);

    $user = $result->fetch_assoc();
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<meta name="Description" content="Enter your description here"/>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
<link rel="stylesheet" href="assets/css/style.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/water.css">
<title>Home</title>
</head>
<body>

    <h1>Home</h1>

    <?php if (isset($user)): ?>
        
        <p>Hello <?= htmlspecialchars($user["name"]) ?></p>

        <p><a href="login.php">Log Out</a></p>

    <?php else: ?>

        <p><a href="templates\login.html">Log In</a> or <a href="templates\signup.html">Sign Up</a></p>

    <?php endif; ?>

</body>
</html>