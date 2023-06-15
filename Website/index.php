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

</script>

<body>
  <div class="starting">
    <h1>Welcome!</h1>
  </div>

  <script src="https://ajax.cloudflare.com/cdn-cgi/scripts/7089c43e/cloudflare-static/rocket-loader.min.js" data-cf-settings="e2e68e2b28a3e84bcc07583e-|49" defer=""></script>


  <!--  the product list title-->
  <div class="bg-page">
    <img class="bg-page-image" src="./img/indexBG.jpg"></img>
  </div>

  <div class="main" id="main">
    <a href="http://localhost/project_new/index.php">
      <img src="./img/hotel_Icon.png" width="100px" height="100px" display="inline-block">
    </a>
    <h1 id="title">City&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspHotel</h1>

    <!--the menu-->

    <div class="menu">

      <li class="item" id="product">
        <a href="#product" class="btn"><i class="fa fa-bed"></i>Room</a>
        <div class="smenu">
          <a href="#" class="sbtn">Computer</a>
          <a href="#" class="sbtn">Phone</a>
          <a href="#" class="sbtn">Cosmetic</a>
        </div>
      </li>

      <li class="item" id="settings">
        <a href="#settings" class="btn"><i class="fa fa-user-secret" aria-hidden="true"></i>Account</a>
        <div class="smenu">
          <a href="#" class="sbtn">Login</a>
          <a href="#" class="sbtn">SignUp</a>
        </div>
      </li>

      <li class="item" id="about">
        <a href="#about" class="btn"><i class="fas fa-info-circle"></i>About</a>
        <div class="smenu">
          <a href="#" class="sbtn">Company</a>
        </div>
      </li>

    </div>

    <?php
      include './sub_php/getDBConnection.php';    
    
      $sql = "SELECT * FROM room_info, room_services where room_info.roomNum = room_services.roomNum;";
      $roomInfo = $conn->query($sql);
    
      $conn->close();    
    ?>

    <table id="productList">
      <thead>
        <tr>
          <th>Hotel Room</th>
          <th>Location</th>
          <th>Price</th>
          <th>Star Rating</th>
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
        <a href="index.html">1</a>
        <a href="index.html" class="active">2</a>
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
