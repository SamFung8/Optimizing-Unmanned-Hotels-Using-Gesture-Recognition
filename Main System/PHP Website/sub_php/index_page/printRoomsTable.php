<?php
  function checkService($message, $value){
    if($value == 1){
      echo "<li>$message&nbsp&nbsp&#9989;</li>";
    }
    else {
      echo "<li>$message&nbsp&nbsp&#10060;</li>";
    }
  }

?>

<?php
  if (!($roomInfo->num_rows > 0)) {
    echo "<script>console.log('No room record.')</script>";
  }
  else {
    while($row = $roomInfo->fetch_assoc()) {
      $roomNum = $row['room_id'];
      $floor = substr($row['room_id'], 0, 2);
      $blk = substr($row['room_id'], 2, 5);
      $roomType = $row['type'];
      $price = $row['price'];
      
      $wifi = $row['wifi'];
      $breakfast = $row['breakfast'];
      $parking = $row['parking'];
      $spa = $row['spa'];

      echo "<tr>
              <td width='30%'><img src='./room_image/$roomNum.jfif' width='400' height='200'></td>
              <td width='10%'>$floor /F, Room $blk</td>
              <td width='10%'>$$price /day</td>
              <td width='10%'>$roomType</td>
              <td width='30%'>
              <ul>
           ";
      
      checkService('Free WiFi', $wifi);
      checkService('Free Breakfast', $breakfast);
      checkService('Free Parking', $parking);
      checkService('Free Spa/Massage', $spa);
        
      echo "
                </ul>
                <a href='./roomBooking.php?ID=$roomNum'><button>Book this room</button></a>
              </td>        
            </tr>";
    }
  }
?>