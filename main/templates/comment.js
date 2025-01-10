// Set current year in footer
document.getElementById('year').textContent = new Date().getFullYear();

// Add back button functionality
function goBack() {
    window.location.href = 'posts.html';
}

// Make sure the function is available before the button is clicked
document.addEventListener('DOMContentLoaded', () => {
    const backButton = document.querySelector('.back-btn');
    if (backButton) {
        backButton.addEventListener('click', goBack);
    }

    // Load post data from sessionStorage
    const post = JSON.parse(sessionStorage.getItem('currentPost'));
    if (post) {
        displayPostDetails(post);
        displayComments(post.comments);
    }

    // Add comment submission handler
    const submitButton = document.getElementById('submitComment');
    submitButton.addEventListener('click', addNewComment);
});

function displayPostDetails(post) {
    document.getElementById('postTitle').textContent = post.title;
    document.getElementById('postAuthor').textContent = post.author;
    document.getElementById('likesCount').textContent = post.likes;
    document.getElementById('dislikesCount').textContent = post.dislikes;

    // Calculate total votes
    const totalVotes = post.options.reduce((sum, option) => sum + option.votes, 0);

    // Display voting options with percentages
    const optionsContainer = document.getElementById('votingOptions');
    optionsContainer.innerHTML = post.options.map(option => {
        const percentage = totalVotes > 0 ? (option.votes / totalVotes * 100).toFixed(1) : 0;
        return `
            <div class="option-result">
                <span class="option-text">${option.text}</span>
                <div class="option-bar">
                    <div class="option-progress" style="width: ${percentage}%"></div>
                    <span class="option-percentage">${percentage}%</span>
                </div>
            </div>
        `;
    }).join('');
}

function displayComments(comments) {
    const commentsContainer = document.getElementById('commentsList');
    commentsContainer.innerHTML = comments.map(comment => {
        const date = new Date(comment.date);
        return `
            <div class="comment">
                <div class="comment-header">
                    <span class="comment-author">${comment.author}</span>
                    <span class="comment-date">${date.toLocaleDateString()}</span>
                </div>
                <div class="comment-content">${comment.content}</div>
            </div>
        `;
    }).join('');
}

function addNewComment() {
    const commentInput = document.getElementById('commentInput');
    const content = commentInput.value.trim();

    if (!content) {
        return;
    }

    const newComment = {
        author: 'Current User', // In a real app, this would come from the logged-in user
        content: content,
        date: new Date().toISOString()
    };

    // Get current post data
    const post = JSON.parse(sessionStorage.getItem('currentPost'));
    post.comments.push(newComment);
    
    // Update storage
    sessionStorage.setItem('currentPost', JSON.stringify(post));
    
    // Refresh comments display
    displayComments(post.comments);
    
    // Clear input
    commentInput.value = '';
}