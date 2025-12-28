// theme-toggle.js - Dark mode toggle and contact modal functionality

// Check for saved theme preference or default to light mode
const currentTheme = localStorage.getItem('theme') || 'light';
document.documentElement.setAttribute('data-theme', currentTheme);

// Toggle theme function
function toggleTheme() {
  const theme = document.documentElement.getAttribute('data-theme');
  const newTheme = theme === 'light' ? 'dark' : 'light';

  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
}

// Contact modal functions
function openContactModal(e) {
  e.preventDefault();
  const overlay = document.getElementById('contact-overlay');
  if (overlay) {
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }
}

function closeContactModal() {
  const overlay = document.getElementById('contact-overlay');
  if (overlay) {
    overlay.classList.remove('active');
    document.body.style.overflow = '';
  }
}

// Add event listener when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', toggleTheme);
  }

  // Contact modal
  const contactBtn = document.getElementById('contact-btn');
  const contactOverlay = document.getElementById('contact-overlay');
  const contactClose = document.getElementById('contact-close');

  if (contactBtn) {
    contactBtn.addEventListener('click', openContactModal);
  }

  if (contactClose) {
    contactClose.addEventListener('click', closeContactModal);
  }

  if (contactOverlay) {
    contactOverlay.addEventListener('click', function(e) {
      if (e.target === contactOverlay) {
        closeContactModal();
      }
    });
  }

  // Close on Escape key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      closeContactModal();
    }
  });
});
