// Set current year in footer
document.getElementById('year').textContent = new Date().getFullYear();

// Add navigation to Liked Votings
document.querySelector('.nav-btn:nth-child(3)').addEventListener('click', () => {
    window.location.href = 'liked.html';
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
const mockMyPosts = [
    {
        id: 1,
        author: 'Current User',
        title: 'Which frontend framework should we use for our new project?',
        options: [
            { text: 'React', votes: 25 },
            { text: 'Vue', votes: 18 },
            { text: 'Angular', votes: 12 },
            { text: 'Svelte', votes: 20 }
        ],
        likes: 30,
        dislikes: 2,
        comments: [
            {
                id: 1,
                author: 'Bob Johnson',
                content: 'React has the largest ecosystem and community support.',
                date: '2024-03-14T15:45:00'
            }
        ]
    }
];