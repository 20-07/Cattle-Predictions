<?php
if(count($_GET)==4)

{

$con=mysqli_connect("localhost:3306","root","$7dev7&7muj7$"); 
$db=mysqli_select_db($con,"Cattle");

if($db)
{

if(isset($_REQUEST['uuid']) && isset($_REQUEST['ubreed'])  && isset($_REQUEST['uage'])   && isset($_REQUEST['ugender'])  )

{
$uid_=$_REQUEST['uuid'];$breed_=$_REQUEST['ubreed'];$gender_=$_REQUEST['ugender']; $age_=$_REQUEST['uage'];
$a="insert into info_cattle (uid,breed,gender,age) values ('$uid_','$breed_','$gender_','$age_') "; 
mysqli_query($con,$a);
}


}

mysqli_close($con);

}

?>