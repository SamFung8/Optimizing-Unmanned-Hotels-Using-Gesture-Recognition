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
      $roomNum = $row['roomNum'];
      $blk = $row['blk'];
      $floor = $row['floor'];
      $starRating = $row['starRating'];
      $price = $row['price'];
      
      $wifi = $row['wifi'];
      $breakfast = $row['breakfast'];
      $parking = $row['parking'];
      $spa = $row['spa'];
      $transfer = $row['transfer'];

      echo "<tr>
              <td width='30%'><img src='./room_image/room$roomNum.jfif' width='400' height='200'></td>
              <td width='10%'>$floor /F, BLK $blk</td>
              <td width='10%'>$$price /day</td>
              <td width='10%'>";

      for ($i = 0; $i < $starRating; $i++) {
        echo "<span class='fa fa-star checked'></span>";
      }              
      for ($i = 5 - $starRating; $i > 0; $i--) {
        echo "<span class='fa fa-star'></span>";
      }              

      echo "  </td>
              <td width='30%'>
                <ul>
           ";
      
      checkService('Free WiFi', $wifi);
      checkService('Breakfast', $breakfast);
      checkService('Parking', $parking);
      checkService('Spa/Massage', $spa);
      checkService('Private transfers', $transfer);
        
      echo "
                </ul>
                <a href='./roomInfo.php?ID=$roomNum'><button>Show more information</button></a>
              </td>        
            </tr>";
    }
  }
?>