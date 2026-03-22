// Phone Numbers Dropdown
const phoneToggle = document.getElementById('phoneToggle');
const phoneMenu = document.getElementById('phoneMenu');

if (phoneToggle && phoneMenu) {
  phoneToggle.addEventListener('click', (e) => {
    e.stopPropagation();
    phoneMenu.classList.toggle('open');
    phoneToggle.classList.toggle('active');
  });
}

// Search Overlay
const searchOpen = document.getElementById('searchOpen');
const searchOverlay = document.getElementById('searchOverlay');
const searchClose = document.getElementById('searchClose');
const searchInput = document.getElementById('searchInput');

if (searchOpen && searchOverlay && searchClose && searchInput) {
  searchOpen.addEventListener('click', () => {
    searchOverlay.classList.add('open');
    setTimeout(() => searchInput.focus(), 350);
  });

  searchClose.addEventListener('click', () => {
    searchOverlay.classList.remove('open');
  });

  searchOverlay.addEventListener('click', (e) => {
    if (e.target === searchOverlay) {
      searchOverlay.classList.remove('open');
    }
  });
}

// ESC key closes overlays
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    if (searchOverlay) searchOverlay.classList.remove('open');
    if (phoneMenu) phoneMenu.classList.remove('open');
    if (phoneToggle) phoneToggle.classList.remove('active');
    const mobileNav = document.getElementById('mobileNav');
    if (mobileNav) mobileNav.classList.remove('open');
    document.body.style.overflow = '';
  }
});

// Close phone dropdown on outside click
document.addEventListener('click', (e) => {
  const phoneDropdown = document.getElementById('phoneDropdown');
  if (phoneDropdown && !phoneDropdown.contains(e.target)) {
    if (phoneMenu) phoneMenu.classList.remove('open');
    if (phoneToggle) phoneToggle.classList.remove('active');
  }
});

// Mobile Nav
const hamburger = document.getElementById('hamburger');
const mobileNav = document.getElementById('mobileNav');
const mobileNavClose = document.getElementById('mobileNavClose');

if (hamburger && mobileNav) {
  hamburger.addEventListener('click', () => {
    mobileNav.classList.add('open');
    document.body.style.overflow = 'hidden';
  });
}

if (mobileNavClose && mobileNav) {
  mobileNavClose.addEventListener('click', () => {
    mobileNav.classList.remove('open');
    document.body.style.overflow = '';
  });
}

// Mobile sub-menu toggles
document.querySelectorAll('.mobile-nav__link[data-toggle]').forEach(btn => {
  btn.addEventListener('click', () => {
    const targetId = btn.getAttribute('data-toggle');
    const submenu = document.getElementById(targetId);
    if (submenu) {
      const isOpen = submenu.classList.contains('open');

      // Close all
      document.querySelectorAll('.mobile-nav__sub').forEach(s => s.classList.remove('open'));
      document.querySelectorAll('.mobile-nav__link').forEach(b => b.classList.remove('expanded'));

      if (!isOpen) {
        submenu.classList.add('open');
        btn.classList.add('expanded');
      }
    }
  });
});

// Sticky navbar shrink effect on scroll
const navbar = document.getElementById('navbar');
if (navbar) {
  let lastScroll = 0;

  window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll > 10) {
      navbar.style.boxShadow = '0 2px 20px rgba(0,0,0,0.1)';
    } else {
      navbar.style.boxShadow = 'var(--shadow-sm)';
    }

    lastScroll = currentScroll;
  });
}
