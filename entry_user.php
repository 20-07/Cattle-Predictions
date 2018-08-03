<?php
if(count($_GET)==2)

{

$con=mysqli_connect("localhost:3306","root","$7dev7&7muj7$"); 
$db=mysqli_select_db($con,"Cattle");

if($db)
{

if(isset($_REQUEST['uname']) && isset($_REQUEST['uaad']) )

{
$name=$_REQUEST['uname'];$num=$_REQUEST['uaad'];
$a="insert into info_owner (aadhar,name) values ('$num','$name') "; 
mysqli_query($con,$a);
}


}

mysqli_close($con);

}

?>