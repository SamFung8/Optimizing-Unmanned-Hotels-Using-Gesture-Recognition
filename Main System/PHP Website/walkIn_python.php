<!DOCTYPE html>
<html>

<head>
  <title></title>
  <style>
    body {
      margin: 0;
      padding: 0;
      background-color: #ffffff;
    }

    .box {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }

    h1 {
      position: absolute;
      top: 35%;
      left: 50%;
      transform: translate(-50%, -50%);
    }

    .box select {
      background-color: #0563af;
      color: white;
      padding: 12px;
      width: 250px;
      border: none;
      font-size: 20px;
      box-shadow: 0 5px 25px rgba(0, 0, 0, 0.2);
      -webkit-appearance: button;
      appearance: button;
      outline: none;
    }

    .box::before {
      content: "\25BC";
      font-family: FontAwesome;
      position: absolute;
      top: 0;
      right: 0;
      width: 20%;
      height: 100%;
      text-align: center;
      font-size: 28px;
      line-height: 45px;
      color: rgba(255, 255, 255, 0.5);
      background-color: rgba(255, 255, 255, 0.1);
      pointer-events: none;
    }

    .box:hover::before {
      color: rgba(255, 255, 255, 0.6);
      background-color: rgba(255, 255, 255, 0.2);
    }

    .box select option {
      padding: 30px;
    }

    .button {
      background-color: #4CAF50;
      /* Green */
      border: none;
      color: white;
      padding: 15px 32px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;

      position: absolute;
      top: 50%;
      left: 80%;
      transform: translate(-50%, -50%);
    }

  </style>
</head>

<body>

  <h1>Please select the room type you when to find!</h1>
  <form action="./roomInfo_python.php" method="GET">
    <div class="box">
      <select name='roomType'>
        <option value="Single Room">Single Room</option>
        <option value="Twin Room">Twin Room</option>
        <option value="Double Room">Double Room</option>
        <option value="Triple Room">Triple Room</option>
        <option value="King Room">King Room</option>
      </select>
    </div>
    <button type="submit" class="button">Search</button>
  </form>
</body>

</html>
