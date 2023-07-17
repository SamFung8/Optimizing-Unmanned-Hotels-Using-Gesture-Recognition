<!DOCTYPE html>
<html>

<head>
  <title>Online Hotel Booking</title>
  <link rel="stylesheet" href="./css/index_page/menu.css">
  <link rel="stylesheet" href="./css/index_page/productList.css">
  <link rel="stylesheet" href="./css/index_page/pageNumbering.css">
  <link rel="stylesheet" href="./css/index_page/designTitle.css">
  <link rel="stylesheet" href="./css/index_page/star.css">
  <link rel="stylesheet" href="./css/index_page/contact.css">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css">
  <link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Lobster">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js" type="e2e68e2b28a3e84bcc07583e-text/javascript"></script>

</head>


<body>
  <script src="https://ajax.cloudflare.com/cdn-cgi/scripts/7089c43e/cloudflare-static/rocket-loader.min.js" data-cf-settings="e2e68e2b28a3e84bcc07583e-|49" defer=""></script>

  <div class="starting">
    <h1>Welcome!</h1>
  </div>
  
 <?php
  if (!isset($_COOKIE['firsttime']))
  {
      setcookie("firsttime", 86400);
      echo '
      <script type="e2e68e2b28a3e84bcc07583e-text/javascript">
        window.setTimeout(function() {
          $(".starting").fadeOut(800)
        }, 0);
        window.setTimeout(function() {
          $(".bg-page").fadeIn(800)
        }, 1000);
        window.setTimeout(function() {
          $(".main").fadeIn(1500)
        }, 2000);
      </script>';
  }else{
      echo ' 
      <script type="e2e68e2b28a3e84bcc07583e-text/javascript">
        window.setTimeout(function() {
          $(".starting").fadeOut(0)
        }, 0);
        window.setTimeout(function() {
          $(".bg-page").fadeIn(0)
        }, 0);
        window.setTimeout(function() {
          $(".main").fadeIn(0)
        }, 0);
      </script>';
  }
 ?>
 
<script>
function showSearchBox() {
  document.getElementById("searchBox").style.display = "block";
}
</script>



  <!--  the product list title-->

  <div class="main" id="main">
    <a href="http://localhost/project_new/index.php">
      <img src="./img/hotel_Icon.png" width="100px" height="100px" display="inline-block">
    </a>
    <h1 id="title">City&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspHotel</h1>

    <!--the menu-->

    <div class="menu">

      <li class="item" id="product">
        <a href="./index.php" class="btn"><i class="fa fa-bed"></i>Home Page</a>
      </li>

      <li class="item" id="settings">
        <a onclick="showSearchBox()" class="btn"><i class="fa fa-search" aria-hidden="true"></i>Advanced Search</a>
      </li>

      <li class="item" id="about">
        <a href="#about" class="btn"><i class="fas fa-info-circle"></i>About</a>
        <div class="smenu">
          <a href="#" class="sbtn">Company</a>
        </div>
      </li>

    </div>

    <?php
      function checkServices($name){
        if (isset($_GET[$name])){
          return ("room_service.".$name." = 1");
        }else{
          return ("room_service.".$name." = 0");
        }
      }
    
    
      include './sub_php/getDBConnection.php';    
    
      if (!isset($_GET['type'])){
        $sql = "SELECT * FROM room_information, room_service where room_information.room_id = room_service.room_id;";
      }else{
        $sql = "SELECT * FROM room_information, room_service where room_information.room_id = room_service.room_id and
                room_information.type = '".$_GET['type']."' and ".
                checkServices('wifi')." and ".
                checkServices('breakfast')." and ".
                checkServices('parking')." and ".
                checkServices('spa').
                ";";
      }
      $roomInfo = $conn->query($sql);
    
      $conn->close();    
    ?>
    
    <div id='searchBox' style="background-color:rgb(232, 176, 74);text-align: center;display: none;">
      <h2>Advanced Search</h2>
        <form action='./index.php'>
         <h3 style="text-align: left;">
           Services
         </h3>
         <table style="width:80%">
         <tr>
          <td><input type="checkbox" name="wifi" value="1">
          <label>WiFi</label><br></td>
          <td><input type="checkbox" name="breakfast" value="1">
          <label>Breakfast</label><br></td>
          <td><input type="checkbox" name="parking" value="1">
          <label>Parking</label><br></td>
          <td><input type="checkbox" name="spa" value="1">
          <label>Spa</label><br></td>
         </tr></table>
         <table style="width:70%">
        <tr>
         <h3 style="text-align: left;">
           Room Type
         </h3>
          <td><input type="radio" name="type" value="Single Room"  checked="checked">
          <label>Single Room</label><br></td>
          <td><input type="radio" name="type" value="1">
          <label>Breakfast</label><br></td>
          <td><input type="radio" name="type" value="1">
          <label>Parking</label><br></td>
          <td><input type="radio" name="type" value="1">
          <label>Spa</label><br></td>
        </tr>
      </table>
      <br>
      <input type="submit" value="Search">
      </form>
    </div>
    
    
    

    <table id="productList">
      <thead>
        <tr>
          <th>Hotel Room</th>
          <th>Location</th>
          <th>Price</th>
          <th>Room Type</th>
          <th>Services</th>
        </tr>
      </thead>
      <hr>
      <tbody>

        <?php
          include './sub_php/index_page/printRoomsTable.php'; 
        ?>

      </tbody>
    </table>


    <!--the page number-->
    <div class="center">
      <div class="pagination">
        <a href="index.html">&laquo;</a>
        <a href="index.html" class="active">1</a>
        <a href="index.html">2</a>
        <a href="index.html">3</a>
        <a href="index.html">&raquo;</a>
      </div>
    </div>


    <!--the contact icon and button-->
    <div class="contact">
      <a class="btn" href="https://facebook.com" target="_blank">
        <i class="fab fa-facebook-f"></i>
      </a>
      <a class="btn" href="https://www.twitter.com" target="_blank">
        <i class="fab fa-twitter"></i>
      </a>
      <a class="btn" href="https://www.gmail.com" target="_blank">
        <i class="fab fa-google"></i>
      </a>
      <a class="btn" href="https://www.instagram.com" target="_blank">
        <i class="fab fa-instagram"></i>
      </a>
      <a class="btn" href="https://www.youtube.com" target="_blank">
        <i class="fab fa-youtube"></i>
      </a>
    </div>
  </div>

</body>

</html>
