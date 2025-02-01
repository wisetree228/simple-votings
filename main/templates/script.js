// Set current year in footer
document.getElementById('year').textContent = new Date().getFullYear();

// Add button click handlers
document.querySelectorAll('.btn').forEach(button => {
    button.addEventListener('click', function() {
        const action = this.textContent.toLowerCase();
        if (action === 'register') {
            window.location.href = 'register.html';
        } else if (action === 'sign in') {
            window.location.href = 'login.html';
        }
    });
});