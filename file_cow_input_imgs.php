<!DOCTYPE html>
<html>
<body     bgcolor="#000">

<?php
if( count($_GET)==1  &&  isset($_REQUEST['uaad']))
 $var_value = $_REQUEST['uaad'];
?>
<h1 style="color:white; margin-top:10%; font-size:45px">*Upload imgs in 12seconds</h1> 

<form   onsubmit="myFunction1()"         method="post" enctype="multipart/form-data"   >
  <div style=" text-align:center;height:11vh; margin-top:30%; margin-left:40%;">  <h1 style="color:white; font-size:65px;">Fview >></h1>   <input type="file"  accept="image/*" capture="capture"     name="fileToUpload1" id="fileToUpload1"  style="font-size:84px;backgroung-color:#F00;">
    <br></div>
  <div style=" text-align:center;height:11vh; margin-top:-7%; margin-left:100%;">
     <input type="submit"     value="Upload" name="submit" size="30"  style="color:black; font-size:65px; background-color:#9c0; width:150p; border-radius:10%; padding:30px;" >
        </div>
</form>

<form   onsubmit="myFunction2()"             method="post" enctype="multipart/form-data"   >
  <div style=" text-align:center;height:11vh; margin-top:20%; margin-left:40%;">  <h1 style="color:white; font-size:65px;">Muzzle >></h1>   <input type="file"  accept="image/*" capture="capture"     name="fileToUpload2" id="fileToUpload2"  style="font-size:84px;backgroung-color:#F00;">
    <br></div>
  <div style=" text-align:center;height:11vh; margin-top:-7%; margin-left:100%;">
     <input type="submit" value="Upload" name="submit" size="30"  style="color:black; font-size:65px; background-color:#9c0; width:150p; border-radius:10%; padding:30px;" >
        </div>
</form>

<form   onsubmit="myFunction3()"             method="post" enctype="multipart/form-data"   >
  <div style=" text-align:center;height:11vh; margin-top:20%; margin-left:40%;"> <h1 style="color:white; font-size:65px;">Side View >></h1> <input type="file" accept="image/*" capture="capture"     name="fileToUpload3" id="fileToUpload3"  style="font-size:84px;backgroung-color:#F00;">
    <br></div>
  <div style=" text-align:center;height:11vh; margin-top:-7%; margin-left:100%;">
     <input type="submit" value="Upload" name="submit" size="30"  style="color:black; font-size:65px; background-color:#9c0; width:150p; border-radius:10%; padding:30px;" >
        </div>

</form>
<h1 style="color:white; margin-top:40%; font-size:45px">*Open Back the App after uploading all images</h1> 


<script>
function myFunction1() {
alert("Front view Image Submitted");
<?php
$temp = $_FILES["fileToUpload1"]["tmp_name"];
$image = basename($_FILES["fileToUpload1"]["name"]);
$image=$var_value;
$image=$image.'.jpg';
$img = "validation_predict_cow/fview/".$image;
move_uploaded_file($temp, $img);
?>
alert("Fview Image Submitted");
}


function myFunction2() {
<?php
$temp = $_FILES["fileToUpload2"]["tmp_name"];
$image = basename($_FILES["fileToUpload2"]["name"]);
$image=$var_value;
$image=$image.'.jpg';
$img = "validation_predict_cow/muzzle/".$image;
move_uploaded_file($temp, $img);
?>
alert("Muzzle Image Submitted");
}


function myFunction3() {
<?php
$temp = $_FILES["fileToUpload3"]["tmp_name"];
$image = basename($_FILES["fileToUpload3"]["name"]);
$image=$var_value;
$image=$image.'.jpg';
$img = "validation_predict_cow/LorRview/".$image;
move_uploaded_file($temp, $img);
?>
alert("Side View Image Submitted");
}

</script>


</body>
</html>





