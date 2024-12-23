export function setupButtonHandlers() {
    const buttons = {
        profile: document.getElementById('profileBtn'),
        register: document.getElementById('registerBtn'),
        login: document.getElementById('loginBtn')
    };

    buttons.profile.addEventListener('click', () => {
        alert('Profile button clicked');
    });

    buttons.register.addEventListener('click', () => {
        alert('Registration button clicked');
    });

    buttons.login.addEventListener('click', () => {
        alert('Authorization button clicked');
    });
}