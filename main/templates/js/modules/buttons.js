export function initializeButtons() {
    const buttons = {
        profile: document.getElementById('profileBtn'),
        register: document.getElementById('registerBtn'),
        login: document.getElementById('loginBtn')
    };

    setupButtonHandlers(buttons);
}

function setupButtonHandlers(buttons) {
    buttons.profile.addEventListener('click', handleProfileClick);
    buttons.register.addEventListener('click', handleRegisterClick);
    buttons.login.addEventListener('click', handleLoginClick);
}

function handleProfileClick() {
    alert('Profile button clicked');
}

function handleRegisterClick() {
    window.location.href = '/register.html';
}

function handleLoginClick() {
    window.location.href = '/login.html';
}