<!DOCTYPE html>
<html>

<head>
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css">
  <link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Lobster">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="./css/room_info/button.css">

  <style>
    .title {
      text-align: center;
    }
  </style>
</head>

<body>
 <?php
    $counter = 0;
    $totalItems = 0;
  ?>
 

 
 
 
  <?php
    include './sub_php/getDBConnection.php';

    $sql = "SELECT * FROM room_information, room_service where room_information.type = '". $_GET['roomType']. "' and room_service.room_id = room_information.room_id;";
    $roomInfo = $conn->query($sql);

    $conn->close();
?>
  <?php
  function checkService($message, $value){
    if($value == 1){
      return "<li>$message&nbsp&nbsp&#9989;</li>";
    }
    else {
      return "<li>$message&nbsp&nbsp&#10060;</li>";
    }
  }
?>

  <?php
  while($row = $roomInfo->fetch_assoc()){
  
    $roomNum[$counter] = $row['room_id'];
    $floor[$counter] = substr($row['room_id'], 0, 2);
    $blk[$counter] = substr($row['room_id'], 2, 5);
    $starRating[$counter] = $row['star_rating'];
    $roomType[$counter] = $row['type'];
    $roomSize[$counter] = $row['size'];
    $price[$counter] = $row['price'];

    $wifi[$counter] = $row['wifi'];
    $breakfast[$counter] = $row['breakfast'];
    $parking[$counter] = $row['parking'];
    $spa[$counter] = $row['spa'];
    
    
    $items[$counter] = "<div id='item'><h3 class='title' name='id' value='". $roomNum[$counter]. "'>Room ID:". $roomNum[$counter]. "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp". $floor[$counter]. "/F, Room ". $blk[$counter]. "</h3>";
  
    $items[$counter] .= "<table style='width:auto'><tr><td>
    <div style= 'margin-bottom: 20px;'><img src='./room_image/$roomNum[$counter].jfif' width='500' height='300'></div>
      <div style= 'margin-left: 100px;'>";
      $items[$counter] .= checkService('Free WiFi', $wifi[$counter]);
      $items[$counter] .= checkService('Breakfast', $breakfast[$counter]);
      $items[$counter] .= checkService('Parking', $parking[$counter]);
      $items[$counter] .= checkService('Spa/Massage', $spa[$counter]);
      $items[$counter] .= "<li>Star Rating: ";
      for ($i = 0; $i < $starRating[$counter]; $i++) {
          $items[$counter] .= "<span class='fa fa-star checked'></span>";
        }              
      $items[$counter] .= "</li>";
      $items[$counter] .= "<li>Room Type: $roomType[$counter]</li>";
      $items[$counter] .= "<li>Room Size: $roomSize[$counter]</li>";

    $url = '"./bookingInfoWalkIn_python.php?roomNum='.$roomNum[$counter].'"';
    $items[$counter] .= "<h3>Price per Day: $". $price[$counter]. " </h3></div>
      </td><td><table style='width:auto'>
      <tr><button style='width: 200px' class='button-85' role='button' onclick='changeItem(-1)'>Previous Room</button></tr>
      <tr><button style='width: 200px' class='button-85' role='button' onclick='window.location.href = ".$url."'>Book This Room</button></tr>
      <tr><button style='width: 200px' class='button-85' role='button' onclick='changeItem(+1)'>Next <br> Room</button></tr>
      </table></td></tr></table></div>"; 
    
    $counter++;
    $totalItems++;
    
    
  }
  $counter--;
  $totalItems--;
  ?>
        
  <?php  echo $items[$counter];
  ?>
  

<script>
    var items = <?php echo json_encode($items); ?>;
    var counter = <?php echo json_encode($counter); ?>;
    var totalItems = <?php echo json_encode($totalItems); ?>;
  
    function changeItem(current)
    {
      
      counter = counter + current;
      if(counter > totalItems)
      {
        counter = 0;
      }
      
      if(counter < 0)
      {
        counter = totalItems;
      }
      
      document.getElementById("item").innerHTML = items[counter];
    }
  </script>

</body>

</html>
