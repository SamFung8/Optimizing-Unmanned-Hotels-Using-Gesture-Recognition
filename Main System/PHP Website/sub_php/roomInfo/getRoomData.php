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
  $row = $roomInfo->fetch_assoc();
  
  $roomNum = $row['room_id'];
  $floor = substr($row['room_id'], 0, 2);
  $blk = substr($row['room_id'], 2, 5);
  $starRating = $row['star_rating'];
  $roomType = $row['type'];
  $roomSize = $row['size'];
  $price = $row['price'];

  $wifi = $row['wifi'];
  $breakfast = $row['breakfast'];
  $parking = $row['parking'];
  $spa = $row['spa'];


  echo  "<div style= 'margin-bottom: 20px;'><img src='./room_image/$roomNum.jfif' width='500' height='300'></div>
        <div style= 'margin-left: 100px;'>";
        checkService('Free WiFi', $wifi);
        checkService('Breakfast', $breakfast);
        checkService('Parking', $parking);
        checkService('Spa/Massage', $spa);
        echo "<li>Star Rating: ";
        for ($i = 0; $i < $starRating; $i++) {
            echo "<span class='fa fa-star checked'></span>";
          }              
        echo "</li>";
        echo "<li>Room Type: $roomType</li>";
        echo "<li>Room Size: $roomSize</li></div>";

  echo  "<div><h3>Price per Day: $". $price. " </h3></div>";
?>
