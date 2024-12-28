// Set current year in footer
document.getElementById('year').textContent = new Date().getFullYear();

// Mock data for demonstration
const mockPosts = [
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
            },
            {
                id: 2,
                author: 'Bob Johnson',
                content: 'Python is great for beginners and professionals alike.',
                date: '2024-03-15T11:15:00'
            }
        ]
    },
    {
        id: 2,
        author: 'Jane Smith',
        title: 'Which framework should we use for our next project?',
        options: [
            { text: 'React', votes: 28 },
            { text: 'Vue', votes: 22 },
            { text: 'Angular', votes: 15 },
            { text: 'Svelte', votes: 18 }
        ],
        likes: 28,
        dislikes: 3,
        comments: [
            {
                id: 1,
                author: 'Charlie Brown',
                content: 'React has the largest ecosystem and community support.',
                date: '2024-03-15T09:45:00'
            }
        ]
    }
];

// Create post HTML
function createPostElement(post) {
    const postElement = document.createElement('div');
    postElement.className = 'post';
    postElement.innerHTML = `
        <div class="post-header">
            <span class="post-author">${post.author}</span>
        </div>
        <h3 class="post-title">${post.title}</h3>
        <div class="voting-options">
            ${post.options.map((option, index) => `
                <div class="voting-option">
                    <input type="radio" id="option${post.id}_${index}" name="post${post.id}" value="${option.text}">
                    <label for="option${post.id}_${index}">${option.text}</label>
                </div>
            `).join('')}
        </div>
        <div class="post-actions">
            <button class="action-btn like-btn" data-post-id="${post.id}">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M7 10v12"></path>
                    <path d="M15 5.88 14 10h5.83a2 2 0 0 1 1.92 2.56l-2.33 8A2 2 0 0 1 17.5 22H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h2.76a2 2 0 0 0 1.79-1.11L12 2h0a3.13 3.13 0 0 1 3 3.88Z"></path>
                </svg>
                <span>${post.likes}</span>
            </button>
            <button class="action-btn dislike-btn" data-post-id="${post.id}">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M17 14V2"></path>
                    <path d="M9 18.12 10 14H4.17a2 2 0 0 1-1.92-2.56l2.33-8A2 2 0 0 1 6.5 2H20a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-2.76a2 2 0 0 0-1.79 1.11L12 22h0a3.13 3.13 0 0 1-3-3.88Z"></path>
                </svg>
                <span>${post.dislikes}</span>
            </button>
            <button class="action-btn comment-btn" data-post-id="${post.id}" onclick="goToComments(${post.id})">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                </svg>
                <span>${post.comments.length}</span>
            </button>
        </div>
    `;

    return postElement;
}

// Initialize posts
function initializePosts() {
    const postsContainer = document.getElementById('postsContainer');
    mockPosts.forEach(post => {
        postsContainer.appendChild(createPostElement(post));
    });
}

// Navigate to comments page
function goToComments(postId) {
    // Store the current post data in sessionStorage so it's available on the comments page
    const post = mockPosts.find(p => p.id === postId);
    sessionStorage.setItem('currentPost', JSON.stringify(post));
    window.location.href = `comment.html?id=${postId}`;
}

// Search functionality
document.getElementById('searchInput').addEventListener('input', (e) => {
    const searchTerm = e.target.value.toLowerCase();
    const posts = document.querySelectorAll('.post');
    
    posts.forEach(post => {
        const title = post.querySelector('.post-title').textContent.toLowerCase();
        post.style.display = title.includes(searchTerm) ? 'block' : 'none';
    });
});

// Handle voting actions
document.addEventListener('click', (e) => {
    if (e.target.closest('.action-btn')) {
        const button = e.target.closest('.action-btn');
        if (button.classList.contains('like-btn') || button.classList.contains('dislike-btn')) {
            const countSpan = button.querySelector('span');
            const currentCount = parseInt(countSpan.textContent);
            countSpan.textContent = currentCount + 1;
            button.classList.add('active');
        }
    }
});

// Initialize the page
initializePosts();