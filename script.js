/* ===== CU Motorsports — Main JavaScript ===== */

// ---- Preloader ----
window.addEventListener('load', () => {
  setTimeout(() => {
    document.getElementById('preloader').classList.add('hide');
  }, 1200);
});

// ---- Navbar scroll effect ----
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 60);
});

// ---- Mobile menu ----
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');
hamburger.addEventListener('click', () => {
  hamburger.classList.toggle('open');
  navLinks.classList.toggle('open');
});
navLinks.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    hamburger.classList.remove('open');
    navLinks.classList.remove('open');
  });
});

// ---- Active nav link on scroll ----
const sections = document.querySelectorAll('section[id]');
window.addEventListener('scroll', () => {
  const scrollY = window.scrollY + 120;
  sections.forEach(section => {
    const top = section.offsetTop;
    const height = section.offsetHeight;
    const id = section.getAttribute('id');
    const link = navLinks.querySelector(`a[href="#${id}"]`);
    if (link) {
      if (scrollY >= top && scrollY < top + height) {
        navLinks.querySelectorAll('a').forEach(a => a.classList.remove('active'));
        link.classList.add('active');
      }
    }
  });
});

// ---- Scroll reveal ----
const revealElements = document.querySelectorAll('.reveal');
const revealOnScroll = () => {
  revealElements.forEach(el => {
    const top = el.getBoundingClientRect().top;
    if (top < window.innerHeight - 80) {
      el.classList.add('active');
    }
  });
};
window.addEventListener('scroll', revealOnScroll);
window.addEventListener('load', revealOnScroll);
