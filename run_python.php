<?php
    date_default_timezone_set('America/Chicago');
    $dir = $_SERVER['DOCUMENT_ROOT'];


    $file = $_FILES['uploadedfile']['tmp_name'];
    $names = $_FILES['uploadedfile']['name'];

    $target = $dir.'/In/'.$names;
    move_uploaded_file( $_FILES['uploadedfile']['tmp_name'], $target);

    $command = escapeshellcmd("python2.7 read.py $target");
    $output = json_decode(shell_exec($command), true);
    echo "<pre>";
    echo "something";
    echo $output;
    echo '<a href="'.$output['file'].'">Download Report</a>';
    echo "</pre>";

//  Re-route to directory to download the file.
//    $domain = $_SERVER['HTTP_HOST'];
//    $path = implode("/",$fullPath);
//    $toLogin = 'http://'.$domain.$path."/out";
//    header('Location:'.$toLogin);
?>