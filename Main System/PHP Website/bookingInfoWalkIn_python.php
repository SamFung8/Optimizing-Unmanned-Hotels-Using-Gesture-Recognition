<!DOCTYPE html>
<html>

<head>
  <title></title>
  <link rel="stylesheet" href="./css/room_info/style.css">
  <style>

  </style>
</head>

<body>

  <div class="container" style="width:90%;height:50%;">
    <form action="./loading_python.php" method="get">
      <div class="title">Booking Registration</div>
      <?php $roomNum=$_GET['roomNum'];
            $floor = substr($roomNum, 0, 2);
            $blk = substr($roomNum, 2, 5);
            echo "<input type='hidden' name='id' value='". $roomNum. "'>
            <h3 name='id' value='". $roomNum. "'>Room ID:". $roomNum. "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp". $floor. "/F, Room ". $blk. "</h3>"; ?>
      <div class="content">
        <div class="user-details">
          <div class="input-box">
            <span class="details">Full Name</span>
            <input type="text" placeholder="Enter your name" name="name" required>
          </div>
          <div class="input-box">
            <span class="details">Phone Number</span>
            <input type="number" placeholder="Enter your number" name="phoneNum" required>
          </div>
          <div class="input-box">
            <span class="details">Check-in Time</span>
            <input type="datetime-local" placeholder="Choose your time" name="inTime" required>
          </div>
          <div class="input-box">
            <span class="details">Check-out Time</span>
            <input type="datetime-local" placeholder="Choose your time" name="outTime" required>
          </div>
        </div>
        <div class="button">
          <input type="submit" value="Book">
        </div>
      </div>  
    </form>
  </div>

</body>

</html>
