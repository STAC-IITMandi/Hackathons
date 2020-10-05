<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>




<?php
// define variables and set to empty values
$lat = $long = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $lat = test_input($_POST["lat"]);
  $long = test_input($_POST["long"]);
}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?>

<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
  Latitude:<br>
  <input type="text" name="lat" >
  <br>
  Longitude:<br>
  <input type="text" name="long" >
  <br><br>
  <input type="submit" value="Submit">
</form> 

<?php
echo "<h2>Your Input:</h2>";
echo $lat;
echo "<br>";
echo $long;
echo "<br>";
?>

<?php


$file = fopen("/var/www/html/data.txt","w");
echo fwrite($file,"$lat");
echo fwrite($file,"<br>");
echo fwrite($file,$long);
echo fwrite($file,"<br>");

fclose($file);

$servername = "localhost";
$username = "root";
$password = "Ayush@123";
$dbname = "myDB";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

// $sql = "CREATE TABLE Info (
// id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
// latitude INT(30),
// longitude INT(30),
// )";
$sql = "CREATE TABLE Info (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
latitude FLOAT(30) NOT NULL,
longitude FLOAT(30) NOT NULL
)";

$sql = "INSERT INTO Info (latitude, longitude)
VALUES ($lat, $long)";


if ($conn->query($sql) === TRUE) {
    $last_id = $conn->insert_id;
    echo "New record created successfully. Last inserted ID is: " . $last_id . "<br>";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$sql = "SELECT id, Latitude, longitude FROM Info";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "id: " . $row["id"]. " - Latitude: " . $row["latitude"]. " && Longitude" . $row["longitude"]. "<br>";
    }
} else {
    echo "0 results";
}



// $file = "data.txt";
// $f = fopen($file, 'w'); // Open in write mode

// $sql = mysql_query("SELECT * FROM _$Info");
// if ($conn->query($sql) === TRUE)
// {
// 	echo "New record created------------------------------------------------------------------- ";
// }
// while($row = mysql_fetch_array($sql))
// {
// 	$latitude = $row["latitude"];
//     $longitude = $row["longitude"];

//     $accounts = "$latitude:$longitude<br>";
//     // Or "$user:$pass\n" as @Benjamin Cox points out

//     fwrite($f, $accounts);
// }

// fclose($f);

// echo "<a href=data.txt>TEST!</a>";



$conn->close();
?>




</body>
</html>


