// Set current year in footer
document.getElementById('year').textContent = new Date().getFullYear();

// Handle form submission
document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Get form values
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Basic validation
    if (!email || !password) {
        alert('Please fill in all fields');
        return;
    }

    // Here you would typically validate credentials with a server
    console.log('Login form submitted:', { email });

    // Redirect to posts page after successful login
    window.location.href = 'posts.html';
});