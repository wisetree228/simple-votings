// Update navigation to my votings
document.querySelector('.nav-btn:nth-child(2)').addEventListener('click', () => {
    window.location.href = 'myvotings.html';
});

// Add profile button navigation
document.querySelector('.profile-btn').addEventListener('click', () => {
    window.location.href = 'profile.html';
});

// Add create voting button navigation
document.querySelector('.create-voting-btn').addEventListener('click', () => {
    window.location.href = 'create.html';
});