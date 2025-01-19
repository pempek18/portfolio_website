document.addEventListener('DOMContentLoaded', () => {
    const projectCards = document.querySelectorAll('.project-card');
    const leftColumnContent = document.querySelector('#left_column_content');

    // Check if leftColumnContent exists before setting up event listeners
    if (!leftColumnContent) {
        console.warn('Could not find element with ID "left_column_content"');
        return;
    }

    projectCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            // Get list content if it exists
            const list = card.querySelector('ul')?.innerHTML;
            // Get paragraph content if it exists
            const paragraph = card.querySelector('p')?.innerHTML;
            
            // Build the content based on what exists
            let content = '';
            if (list) content += `<ul>${list}</ul>`;
            if (paragraph) content += `<p>${paragraph}</p>`;
            
            leftColumnContent.innerHTML = content;
        });

        card.addEventListener('mouseleave', () => {
            leftColumnContent.innerHTML = '';
        });
    });
});

function adjustPadding() {
    const projectCard = document.querySelector('.projects-grid');
    const leftColumnContent = document.getElementById('left_column_content');

    if (!projectCard || !leftColumnContent) {
        console.info('Could not find project card or left column content');
        return;
    }
    
    const projectCardHeight = projectCard.offsetHeight;
    const gridRows = Math.ceil(projectCardHeight / 400); // Calculate number of 400px rows
    const minPadding = (10 * 16); // 10rem in pixels (assuming 1rem = 16px)
    const gridPadding = gridRows * 400; // Additional padding based on grid rows
    
    const totalPadding = Math.max(minPadding + gridPadding, projectCardHeight + 20);
    leftColumnContent.style.paddingTop = totalPadding + 'px';
    if (window.innerWidth > 768) {
        leftColumnContent.style.paddingTop = '10rem';
    }
}

// Run on page load
window.addEventListener('load', adjustPadding);

// Run on window resize
window.addEventListener('resize', adjustPadding);