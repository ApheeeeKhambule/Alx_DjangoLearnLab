
// Wait until the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {

    // Form Validation Example
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(event) {
            const email = document.querySelector('input[type="email"]');
            if (email && !email.value.includes('@')) {
                alert('Please enter a valid email address.');
                event.preventDefault(); // Prevent form submission
            }
        });
    }

    // Toggle Menu Example
    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.querySelector('nav ul');
    if (menuToggle && navMenu) {
        menuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
    }

    // Smooth Scroll Example
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Back to Top Button Example
    const backToTopButton = document.querySelector('#back-to-top');
    if (backToTopButton) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 300) {
                backToTopButton.classList.add('visible');
            } else {
                backToTopButton.classList.remove('visible');
            }
        });
        backToTopButton.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
});
