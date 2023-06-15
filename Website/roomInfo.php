<!DOCTYPE html>
<html lang="en" dir="ltr">

<head>
  <meta charset="UTF-8">
  <title> Responsive Registration Form | CodingLab </title>
  <link rel="stylesheet" href="./css/room_info/style.css">
  <link rel="stylesheet" href="./css/room_info/designTitle.css">
  <link rel="stylesheet" href="./css/room_info/button.css">
</head>

<body>

  <table style="width:100%;height:'auto'">
    <tr>
      <td style="width:20%">
        <div><a href="http://localhost/project_new/index.php" >
            <img src="./img/hotel_Icon.png" width="100px"; height="100px"; style="align:center;">
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
        <div>hi</div>
      </td>
      <td>
        <div class="container">
          <div class="title">Booking Registration</div>
          <div class="content">
            <form action="#">
              <div class="user-details">
                <div class="input-box">
                  <span class="details">Full Name</span>
                  <input type="text" placeholder="Enter your name" required>
                </div>
                <div class="input-box">
                  <span class="details">Username</span>
                  <input type="text" placeholder="Enter your username" required>
                </div>
                <div class="input-box">
                  <span class="details">Email</span>
                  <input type="text" placeholder="Enter your email" required>
                </div>
                <div class="input-box">
                  <span class="details">Phone Number</span>
                  <input type="text" placeholder="Enter your number" required>
                </div>
                <div class="input-box">
                  <span class="details">Password</span>
                  <input type="text" placeholder="Enter your password" required>
                </div>
                <div class="input-box">
                  <span class="details">Confirm Password</span>
                  <input type="text" placeholder="Confirm your password" required>
                </div>
              </div>
              <div class="button">
                <input type="submit" value="Register">
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
