export function setupSidebarActions() {
    const sidebarButtons = document.querySelectorAll('.sidebar-btn');
    
    sidebarButtons.forEach(button => {
        button.addEventListener('click', handleSidebarAction);
    });
}

function handleSidebarAction(e) {
    const action = e.target.textContent;
    console.log(`${action} clicked`);
    // Implement sidebar action logic here
}