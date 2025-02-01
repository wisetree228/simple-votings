// Set current year in footer
document.getElementById('year').textContent = new Date().getFullYear();

// Handle adding new options
document.getElementById('addOptionBtn').addEventListener('click', () => {
    const optionsContainer = document.getElementById('optionsContainer');
    const optionCount = optionsContainer.children.length + 1;

    const optionGroup = document.createElement('div');
    optionGroup.className = 'option-group';
    optionGroup.innerHTML = `
        <div class="form-group">
            <input type="text" class="option-input" required>
            <label>Option ${optionCount}</label>
        </div>
        <button type="button" class="remove-option-btn">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M3 6h18"></path>
                <path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"></path>
                <path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"></path>
            </svg>
        </button>
    `;

    optionsContainer.appendChild(optionGroup);
    updateRemoveButtons();
});

// Handle removing options
document.getElementById('optionsContainer').addEventListener('click', (e) => {
    if (e.target.closest('.remove-option-btn')) {
        e.target.closest('.option-group').remove();
        updateLabels();
        updateRemoveButtons();
    }
});

// Update option labels after removal
function updateLabels() {
    const options = document.querySelectorAll('.option-group');
    options.forEach((option, index) => {
        const label = option.querySelector('label');
        label.textContent = `Option ${index + 1}`;
    });
}

// Update remove buttons state
function updateRemoveButtons() {
    const options = document.querySelectorAll('.option-group');
    const removeButtons = document.querySelectorAll('.remove-option-btn');
    
    removeButtons.forEach(button => {
        button.disabled = options.length <= 2;
    });
}

// Handle form submission
document.getElementById('createVotingForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Get form data
    const title = document.getElementById('title').value;
    const votingType = document.querySelector('input[name="votingType"]:checked').value;
    const options = Array.from(document.querySelectorAll('.option-input')).map(input => input.value);

    // Validate
    if (options.some(option => !option.trim())) {
        alert('Please fill in all options');
        return;
    }

    // Create voting object
    const voting = {
        title,
        type: votingType,
        options: options.map(text => ({ text, votes: 0 })),
        author: 'Current User',
        likes: 0,
        dislikes: 0,
        comments: []
    };

    // Here you would typically send the data to a server
    console.log('New voting created:', voting);

    // Redirect back to all votings
    window.location.href = 'posts.html';
});