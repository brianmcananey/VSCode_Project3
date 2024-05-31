<?php

// Show all errors
error_reporting(E_ALL);
ini_set('display_errors', 1);



$host = "localhost";
$dbname = "login_msp3";
$username = "root";
$password = "";

$mysqli = new mysqli(hostname: $host,
                     username: $username,
                     password: $password,
                     database: $dbname);  

if ($mysqli->connect_errno) {
    die("Connection error: " . $mysqli->connect_error);
}

return $mysqli;