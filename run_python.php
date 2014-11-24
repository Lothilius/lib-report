<?php
    date_default_timezone_set('America/Chicago');


    $file = $_FILES['uploadedfile']['tmp_name'];
    $names = $_FILES['uploadedfile']['name'];

    $target = $dir.'In/'.$names;
    move_uploaded_file( $_FILES['uploadedfile']['tmp_name'], $target);

    $command = escapeshellcmd("python read.py $target");
    $output = shell_exec($command);
    echo "<pre>";
    print_r($output);
    echo "</pre>";

//  Re-route to directory to download the file.
//    $domain = $_SERVER['HTTP_HOST'];
//    $path = implode("/",$fullPath);
//    $toLogin = 'http://'.$domain.$path."/out";
//    header('Location:'.$toLogin);
?>