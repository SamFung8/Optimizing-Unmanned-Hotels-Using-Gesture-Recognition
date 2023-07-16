<?php
  include './sub_php/getDBConnection.php';

  $sql = "INSERT INTO MyGuests (firstname, lastname, email) VALUES ('John', 'Doe', 'john@example.com')";
  $roomInfo = $conn->query($sql);

  $conn->close();

  include './sub_php/roomInfo/getRoomData.php'; 
?>
