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

// Mock data for demonstration
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
    },
    {
        id: 2,
        author: 'Current User',
        title: 'What is your preferred code editor?',
        options: [
            { text: 'VS Code', votes: 150 },
            { text: 'WebStorm', votes: 75 },
            { text: 'Sublime Text', votes: 45 },
            { text: 'Vim', votes: 30 }
        ],
        likes: 65,
        dislikes: 8,
        comments: [
            {
                id: 1,
                author: 'Sarah Lee',
                content: 'VS Code with the right extensions is unbeatable!',
                date: '2024-03-15T11:20:00'
            }
        ]
    }
];

// Function to create voting card
function createVotingCard(post) {
    const totalVotes = post.options.reduce((sum, option) => sum + option.votes, 0);
    
    const optionsHtml = post.options.map(option => {
        const percentage = totalVotes > 0 ? (option.votes / totalVotes * 100).toFixed(1) : 0;
        return `
            <div class="voting-option">
                <input type="radio" id="option_${option.text}" name="voting_${post.id}">
                <label for="option_${option.text}">${option.text} (${percentage}%)</label>
            </div>
        `;
    }).join('');

    const card = document.createElement('div');
    card.className = 'post';
    card.innerHTML = `
        <div class="post-header">
            <span class="post-author">${post.author}</span>
        </div>
        <h3 class="post-title">${post.title}</h3>
        <div class="post-content">
            <div class="voting-options">
                ${optionsHtml}
            </div>
        </div>
        <div class="post-actions">
            <button class="action-btn">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M7 10v12"></path>
                    <path d="M15 5.88 14 10h5.83a2 2 0 0 1 1.92 2.56l-2.33 8A2 2 0 0 1 17.5 22H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h2.76a2 2 0 0 0 1.79-1.11L12 2h0a3.13 3.13 0 0 1 3 3.88Z"></path>
                </svg>
                ${post.likes}
            </button>
            <button class="action-btn">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M17 14V2"></path>
                    <path d="M9 18.12 10 14H4.17a2 2 0 0 1-1.92-2.56l2.33-8A2 2 0 0 1 6.5 2H20a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-2.76a2 2 0 0 0-1.79 1.11L12 22h0a3.13 3.13 0 0 1-3-3.88Z"></path>
                </svg>
                ${post.dislikes}
            </button>
            <button class="action-btn" onclick="openComments(${JSON.stringify(post).replace(/"/g, '&quot;')})">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                </svg>
                ${post.comments.length}
            </button>
        </div>
    `;

    return card;
}

// Function to open comments page
function openComments(post) {
    // Store the post data in sessionStorage
    sessionStorage.setItem('currentPost', JSON.stringify(post));
    // Navigate to comments page
    window.location.href = 'comment.html';
}

// Display posts
const postsContainer = document.getElementById('postsContainer');
mockMyPosts.forEach(post => {
    postsContainer.appendChild(createVotingCard(post));
});