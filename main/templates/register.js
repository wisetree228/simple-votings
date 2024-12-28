// Set current year in footer
document.getElementById('year').textContent = new Date().getFullYear();

// Handle form submission
document.getElementById('registrationForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Get form values
    const nickname = document.getElementById('nickname').value;
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    // Basic validation
    if (!nickname || !firstName || !lastName || !email || !password || !confirmPassword) {
        alert('Please fill in all fields');
        return;
    }

    if (password !== confirmPassword) {
        alert('Passwords do not match!');
        return;
    }

    // Here you would typically send the data to a server
    console.log('Registration form submitted:', {
        nickname,
        firstName,
        lastName,
        email
    });

    // Redirect to posts page after successful registration
    window.location.href = 'posts.html';
});