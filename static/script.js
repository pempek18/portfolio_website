document.addEventListener('DOMContentLoaded', () => {
    const projectCards = document.querySelectorAll('.project-card');
    const leftColumnContent = document.querySelector('#left_column_content');

    // Check if leftColumnContent exists before setting up event listeners
    if (!leftColumnContent) {
        console.warn('Could not find element with ID "left_column_content"');
        return;
    }

    // Add click event listener to document to handle clicking outside
    document.addEventListener('click', (event) => {
        // If click is outside any project card, clear selection
        if (!event.target.closest('.project-card')) {
            document.querySelectorAll('.project-card').forEach(card => {
                card.classList.remove('selected');
            });
            leftColumnContent.innerHTML = '';
        }
    });

    projectCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            // Only show hover content if no card is selected
            const selectedCard = document.querySelector('.project-card.selected');
            if (!selectedCard) {
                updateLeftColumn(card);
            }
        });

        card.addEventListener('mouseleave', () => {
            // Only clear content if no card is selected
            const selectedCard = document.querySelector('.project-card.selected');
            if (!selectedCard) {
                leftColumnContent.innerHTML = '';
            }
        });

        card.addEventListener('click', (event) => {
            // Prevent this click from bubbling up to document
            event.stopPropagation();
            
            const wasSelected = card.classList.contains('selected');
            
            // Remove selected class from all cards
            document.querySelectorAll('.project-card').forEach(c => {
                c.classList.remove('selected');
            });

            if (!wasSelected) {
                // Select this card if it wasn't previously selected
                card.classList.add('selected');
                updateLeftColumn(card);
            } else {
                // Clear content if we're unselecting
                leftColumnContent.innerHTML = '';
            }
        });
    });
});

// Helper function to update left column content
function updateLeftColumn(card) {
    // Get list content if it exists
    const list = card.querySelector('ul')?.innerHTML;
    // Get paragraph content if it exists
    const paragraph = card.querySelector('p')?.innerHTML;
    
    // Build the content based on what exists
    let content = '';
    if (list) content += `<ul>${list}</ul>`;
    if (paragraph) content += `<p>${paragraph}</p>`;
    
    leftColumnContent.innerHTML = content;
}