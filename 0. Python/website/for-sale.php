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
                <li><a href="index.html">Home</a></li>
                <li><a href="for-sale.html">For Sale</a></li>
                <li><a href="about.html">About Me</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section class="product-list">
            <?php
            // Include your data.php file for database connection and query
            include("data.php");

            if ($result->num_rows > 0) {
                while ($row = $result->fetch_assoc()) {
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

        <!-- Divider -->
        <div class="divider"></div>
    </main>

    <footer>
        <p>&copy; 2024 Dutch-Aviation.com. All rights reserved.</p>
    </footer>

    <script>
        // Get all product images
        const productImages = document.querySelectorAll('.product img');

        // Get the modal and close button
        const modal = document.querySelector('.modal');
        const closeButton = document.querySelector('.close');
        const modalImage = document.getElementById('modal-image');

        // Function to open the modal
        function openModal(imageSrc) {
            modalImage.src = imageSrc;
            modal.style.display = 'block';

            // Dynamically adjust the image size based on window dimensions
            const maxWidth = window.innerWidth * 0.8;
            const maxHeight = window.innerHeight * 0.8;

            // Set a maximum width and height for the modal image
            if (modalImage.width > maxWidth || modalImage.height > maxHeight) {
                if (modalImage.width / maxWidth > modalImage.height / maxHeight) {
                    modalImage.width = maxWidth;
                    modalImage.height = (modalImage.height * maxWidth) / modalImage.width;
                } else {
                    modalImage.height = maxHeight;
                    modalImage.width = (modalImage.width * maxHeight) / modalImage.height;
                }
            }
        }

        // Function to close the modal
        function closeModal() {
            modal.style.display = 'none';
        }

        // Attach click event listeners to each product image
        productImages.forEach((image) => {
            image.addEventListener('click', () => {
                const imageSrc = image.getAttribute('src');
                openModal(imageSrc);
            });
        });

        // Attach click event listener to the close button
        closeButton.addEventListener('click', closeModal);

        // Close the modal when clicking outside of the image
        window.addEventListener('click', (event) => {
            if (event.target === modal) {
                closeModal();
            }
        });
    </script>

</body>
</html>
