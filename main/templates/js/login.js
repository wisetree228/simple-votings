document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Here you would typically send the data to your server
    console.log('Login data:', { email });
    window.location.href = '/posts.html';
});