// Form Handling Script
document.querySelector('#contact-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const name = document.querySelector('#name').value;
    const email = document.querySelector('#email').value;
    const message = document.querySelector('#message').value;

    if (name && email && message) {
        alert(`Thank you for your message, ${name}! I will get back to you shortly.`);
    } else {
        alert('Please fill in all fields.');
    }
});
