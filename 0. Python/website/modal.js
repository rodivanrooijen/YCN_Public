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