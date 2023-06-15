<!DOCTYPE HTML>
<html>

<head>
  <style>
    .error {
      color: #FF0000;
    }

  </style>
</head>


<?php
// define variables and set to empty values
$nameErr = $emailErr = $genderErr = $websiteErr = "";
$name = $email = $gender = $comment = $website = "";
$inputText = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $inputTest = "true";
    
  if (empty($_POST["name"])) {
    $nameErr = "Name is required";
    $inputTest = "false";
  } else {
    $name = test_input($_POST["name"]);
  }
  
  if (empty($_POST["email"])) {
    $emailErr = "Email is required";
    $inputTest = "false";
  } else {
    $email = test_input($_POST["email"]);
  }

  if (empty($_POST["gender"])) {
    $genderErr = "Gender is required";
    $inputTest = "false";
  } else {
    $gender = test_input($_POST["gender"]);
  }
  
  
  if ($inputTest == "true"){
    header("Location: ./loading.php?name=$name&email=$email");
  }
}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?>

<h2>PHP Form Validation Example</h2>
<p><span class="error">* required field</span></p>


<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
  Name: <input type="text" name="name">
  <span class="error">* <?php echo $nameErr;?></span>
  <br><br>
  E-mail: <input type="text" name="email">
  <span class="error">* <?php echo $emailErr;?></span>
  <br><br>
  Gender:
  <input type="radio" name="gender" value="female">Female
  <input type="radio" name="gender" value="male">Male
  <input type="radio" name="gender" value="other">Other
  <span class="error">* <?php echo $genderErr;?></span>
  <br><br>
  <input type="submit" name="submit" value="Submit">
</form>

</html>
