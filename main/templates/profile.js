// Set current year in footer
document.getElementById('year').textContent = new Date().getFullYear();

// Mock user data - in a real app, this would come from a database
const mockUser = {
    nickname: 'johndoe',
    firstName: 'John',
    lastName: 'Doe',
    email: 'john.doe@example.com',
    avatar: 'https://images.unsplash.com/photo-1633332755192-727a05c4013d?auto=format&fit=crop&w=150&h=150'
};

// Populate form with user data
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('nickname').value = mockUser.nickname;
    document.getElementById('firstName').value = mockUser.firstName;
    document.getElementById('lastName').value = mockUser.lastName;
    document.getElementById('email').value = mockUser.email;
    document.getElementById('avatarPreview').src = mockUser.avatar;

    // Add floating label effect
    document.querySelectorAll('.form-group input').forEach(input => {
        if (input.value) {
            input.classList.add('has-value');
        }
    });
});

// Handle avatar change
document.querySelector('.change-avatar-btn').addEventListener('click', () => {
    document.getElementById('avatarInput').click();
});

document.getElementById('avatarInput').addEventListener('change', function(e) {
    const file = e.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('avatarPreview').src = e.target.result;
        };
        reader.readAsDataURL(file);
    }
});

// Handle form submission
document.getElementById('profileForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const newPassword = document.getElementById('newPassword').value;
    const confirmNewPassword = document.getElementById('confirmNewPassword').value;
    const currentPassword = document.getElementById('currentPassword').value;

    // Validate passwords if trying to change them
    if (newPassword || confirmNewPassword) {
        if (!currentPassword) {
            alert('Please enter your current password to change it');
            return;
        }
        if (newPassword !== confirmNewPassword) {
            alert('New passwords do not match');
            return;
        }
    }

    // Get form data
    const formData = {
        nickname: document.getElementById('nickname').value,
        firstName: document.getElementById('firstName').value,
        lastName: document.getElementById('lastName').value,
        email: document.getElementById('email').value,
        currentPassword: currentPassword,
        newPassword: newPassword
    };

    // Here you would typically send the data to a server
    console.log('Profile update submitted:', formData);

    // Show success message
    alert('Profile updated successfully!');
});