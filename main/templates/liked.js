// Set current year in footer
document.getElementById('year').textContent = new Date().getFullYear();

// Add navigation to My Votings
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

// Mock data for demonstration - in a real app, this would come from a database
const mockLikedPosts = [
    {
        id: 1,
        author: 'John Doe',
        title: 'What is your favorite programming language?',
        options: [
            { text: 'JavaScript', votes: 42 },
            { text: 'Python', votes: 35 },
            { text: 'Java', votes: 28 },
            { text: 'C++', votes: 15 }
        ],
        likes: 42,
        dislikes: 5,
        comments: [
            {
                id: 1,
                author: 'Alice Smith',
                content: 'JavaScript all the way! The ecosystem is unmatched.',
                date: '2024-03-15T10:30:00'
            }
        ]
    }
];