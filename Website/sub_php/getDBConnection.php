<?php
      $servername = "localhost";
      $username = "root";
      $password = "";
      $dbname = "fyp_hotel";

      // Create connection
      $conn = new mysqli($servername, $username, $password, $dbname);

      // Check connection
      if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
      }
      echo "<script>console.log('DB Connected successfully.')</script>";
?>