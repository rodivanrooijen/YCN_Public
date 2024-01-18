<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dutch-Aviation.com</title>
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
                <li><a href="for-sale.php">For Sale</a></li>
                <li><a href="about.html">About Me</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>

        <section class="about">
            <div class="about-content">
                <h2>Welcome to Dutch-Aviation.com</h2>
                <p>I am a passionate aviation enthusiast dedicated to collecting the finest aviation models from around the world. I aim to collect the most exceptional pieces that capture the essence of aviation history.</p>
                <button class="explore-button">Explore My Collection</button>
            </div>
        </section>

        <section class="product-list">
            <?php
            // Include your data.php file for database connection and query
            include("data.php");

            if ($result->num_rows > 0) {
                while ($row = $result->fetch_assoc()) {
                    if ($row["mainpage"] == 1) {
                        echo '<div class="product">';
                        echo '<img class="product-image" src="images/' . $row["img"] . '" alt="' . $row["name"] . '"><br>';
                        echo '<h2>' . $row["name"] . '</h2>';
                        echo '<p class="product-description">' . $row["description"] . '</p>';
                        echo '<p><strong>Price: €' . number_format($row["price"], 2) . '</strong></p>';
                        echo '<a href="contact.html">';
                        echo '<button class="product-button">Contact me!</button>';
                        echo '</a>';
                        echo '</div>';
                    }
                }
            } else {
                echo "No products found.";
            }
            ?>
        </section>

        <div class="modal">
            <div class="modal-content">
                <span class="close">&times;</span>
                <img id="modal-image" src="" alt="Product Image">
            </div>
        </div>

        <section class="fancy-button-section">
            <button class="fancy-button">
                <a href="for-sale.html">Explore More Models for Sale</a>
            </button>
        </section>


        <!-- Divider -->
        <div class="divider"></div>

        
        
    </main>

    <footer>
        <p>&copy; 2024 Dutch-Aviation.com. All rights reserved.</p>
    </footer>

    

    <script src="modal.js"></script>
    
</body>
</html>