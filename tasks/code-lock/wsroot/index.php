<!doctype html>
<html>
<head>
    <title> Security system </title>
</head>
<body>
    <h1>
    <?php
        define('AAA', 1);
        require_once('flag.php');
        if (!isset($_COOKIE['access_code_md5'])) {
            setcookie('access_code_md5', md5('false'));
            echo 'Access Denied';
        } else {
            if ($_COOKIE['access_code_md5'] === md5('true')) {
                echo "Access Granted. The flag is $flag";
            } else {
                setcookie('access_code_md5', md5('false'));
                echo 'Access Denied';
            }
        } 
    ?>
    </h1>
</body>
</html>
