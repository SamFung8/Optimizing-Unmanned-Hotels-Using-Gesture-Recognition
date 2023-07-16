<!DOCTYPE html>
<html>

<head>
  <meta http-equiv='refresh' content='5; URL=./index.php'>
  <style>
    .loader {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }


  </style>
</head>



<body>
    <?php
    include './sub_php/getDBConnection.php';
    $sql = "INSERT INTO customer_information (name, phone_number, email) VALUES ('".$_GET['name']."',".(int)$_GET['phoneNum'].",'".$_GET['email']."');";
    $conn->query($sql);
    $new_customer_id = $conn->insert_id;

    $sql = "INSERT INTO booking_record (customer_id, room_id, check_in_time, check_out_time) VALUES (".$new_customer_id.",'".$_GET['id']."','".
      split("T",$_GET['inTime'])[0]." ".split("T",$_GET['inTime'])[1]. "','".
      split("T",$_GET['outTime'])[0]." ".split("T",$_GET['outTime'])[1]."');";
    $conn->query($sql);
    $new_booking_id = $conn->insert_id;

    $conn->close();
  ?>


  <?php 
  echo shell_exec(
    'python "..\public Machine\Gesture Control\generatQrCode.py" '.
    $new_booking_id.' '.$_GET['email']
  ); ?>

  <div class="starting">
    <div class="loader"><h1>Finshed Booking!</h1></div>
  </div>



</body>


</html>
