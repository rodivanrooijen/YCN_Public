<?php
// Databasegegevens
$servername = "db.dutch-aviation.com";
$username = "md188183db669067";
$password = "Bolle031097!";
$dbname = "md188183db669067";

// Maak een verbinding met de database
$conn = new mysqli($servername, $username, $password, $dbname);

// Controleer de verbinding
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// SQL-query om gegevens op te halen (vervang 'your_table_name' en 'your_column_names')
$sql = "SELECT * FROM airplane_models";
$result = $conn->query($sql);

// Sluit de databaseverbinding niet vergeten als je klaar bent met de query's
$conn->close();
?>