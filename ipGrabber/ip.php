<?php
$ip = date(‘Y-m-d H:i:s’).”  Bot IP: “.$_SERVER[‘REMOTE_ADDR’].”\r\n”;
$fO = fopen(‘log.txt’ , ‘a’);
fwrite($fO, $ip);
fclose($fO);
?>
