<!DOCTYPE html>
<html lang="en" dir="ltr">

<head>
  <meta charset="UTF-8">
  <title> Responsive Registration Form | CodingLab </title>
  <link rel="stylesheet" href="./css/room_info/style.css">
  <link rel="stylesheet" href="./css/room_info/designTitle.css">
  <link rel="stylesheet" href="./css/room_info/button.css">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css">
  <link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Lobster">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>

<body>

  <table style="width:100%;height:'auto'">
    <tr>
      <td style="width:20%">
        <div><a href="http://localhost/project_new/index.php">
            <img src="./img/hotel_Icon.png" width="100px" ; height="100px" ; style="align:center;">
          </a></div>
      </td>
      <td>
        <dir>
          <h1 id="title">Pre&nbsp&nbsp&nbsp&nbsp-&nbsp&nbsp&nbspBooking&nbsp&nbsp&nbsp&nbsp&nbspService</h1>
        </dir>
      </td>
    </tr>
  </table>


  <table style="width:100%;height:'auto'">
    <tr>
      <td style="width:45%">
        <div style= 'margin-left: 80px;>
          <?php
            include './sub_php/getDBConnection.php';

            $sql = "SELECT * FROM room_information, room_service where room_information.room_id = '". $_GET['ID']. "' and room_service.room_id = '". $_GET['ID']. "';";
            $roomInfo = $conn->query($sql);

            $conn->close();
          
            include './sub_php/roomInfo/getRoomData.php'; 
          ?>


        </div>
      </td>
      <td>
        <div class="container">
          <form action="./loading.php" method="get">
            <div class="title">Booking Registration</div>
            <?php echo "<input type='hidden' name='id' value='". $roomNum. "'>
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
                <div class="input-box" style="width:100%;">
                  <span class="details">Email</span>
                  <input type="email" placeholder="Enter your email" name="email" required>
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
            </form>
          </div>
        </div>
      </td>
    </tr>
  </table>

  <!-- HTML !-->
  <button class="button-85" role="button" onclick="history.back()">Previous Page</button>


</body>

</html>
