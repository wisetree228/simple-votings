import { setupVotingActions } from '../components/voting-actions.js';
import { setupThemeFilters } from '../components/theme-filters.js';
import { setupSidebarActions } from '../components/sidebar-actions.js';

document.addEventListener('DOMContentLoaded', () => {
    setupVotingActions();
    setupThemeFilters();
    setupSidebarActions();
});