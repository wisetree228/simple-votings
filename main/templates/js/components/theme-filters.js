export function setupThemeFilters() {
    const themeCheckboxes = document.querySelectorAll('.theme-checkbox input');
    
    themeCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', handleThemeFilter);
    });
}

function handleThemeFilter(e) {
    const theme = e.target.parentElement.textContent.trim();
    const isChecked = e.target.checked;
    
    console.log(`${theme} filter ${isChecked ? 'enabled' : 'disabled'}`);
    // Implement filtering logic here
}