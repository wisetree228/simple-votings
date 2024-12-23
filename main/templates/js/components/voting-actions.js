export function setupVotingActions() {
    const votingCards = document.querySelectorAll('.voting-card');

    votingCards.forEach(card => {
        const likeBtn = card.querySelector('.like-btn');
        const dislikeBtn = card.querySelector('.dislike-btn');
        const commentBtn = card.querySelector('.comment-btn');
        const options = card.querySelectorAll('.option-btn');

        likeBtn?.addEventListener('click', handleLike);
        dislikeBtn?.addEventListener('click', handleDislike);
        commentBtn?.addEventListener('click', handleComment);
        options.forEach(option => {
            option.addEventListener('click', handleVote);
        });
    });
}

function handleLike(e) {
    const count = e.currentTarget.querySelector('span');
    if (count) {
        let likes = parseInt(count.textContent);
        count.textContent = likes + 1;
    }
}

function handleDislike(e) {
    const count = e.currentTarget.querySelector('span');
    if (count) {
        let dislikes = parseInt(count.textContent);
        count.textContent = dislikes + 1;
    }
}

function handleComment() {
    // Implement comment functionality
    console.log('Comment clicked');
}

function handleVote(e) {
    const option = e.currentTarget;
    const options = option.closest('.options').querySelectorAll('.option-btn');
    
    options.forEach(opt => opt.style.borderColor = '#444');
    option.style.borderColor = '#4CAF50';
}