<?php
// Database connection (replace with your database credentials)
$servername = "db.dutch-aviation.com";
$username = "md188183db669067";
$password = "Bolle031097!";
$dbname = "md188183db669067";

$conn = mysqli_connect($db_host, $db_username, $db_password, $db_name);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// Fetch data from the database
$query = "SELECT * FROM airplane_models";
$result = mysqli_query($conn, $query);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>For Sale - Dutch-Aviation.com</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <div class="logo">
                <img src="images/logo.png" alt="Dutch-Aviation.com">
                <h1>Dutch-Aviation.com</h1>
            </div>
            <ul class="menu">
                <li><a href="">Home</a></li>
                <li><a href="for-sale.html">For Sale</a></li>
                <li><a href="about.html">About Me</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section class="product-list">
            <?php
            // Display products dynamically
            while ($row = mysqli_fetch_assoc($result)) {
                echo '<div class="product">';
                echo '<img src="images/' . $row['img_link'] . '" alt="' . $row['img_link'] . '">';
                echo '<h2>' . $row['name'] . '</h2>';
                echo '<p class="product-description">' . $row['description'] . '</p>';
                echo '<p><strong>Price: €' . number_format($row['price'], 2) . '</strong></p>';
                echo '<button class="product-button">Contact me!</button>';
                echo '</div>';
            }
            ?>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Dutch-Aviation.com. All rights reserved.</p>
    </footer>
</body>
</html>

<?php
// Close the database connection
mysqli_close($conn);
?>
