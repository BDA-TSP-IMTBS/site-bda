// animations.js
document.addEventListener('DOMContentLoaded', function () {
    const elements = document.querySelectorAll('.animate');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add(entry.target.classList.contains('right') ? 'fadeInRight' : 'fadeInLeft');
                entry.target.classList.remove('hidden');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });

    elements.forEach(element => {
        element.classList.add('hidden'); // Hide elements initially
        observer.observe(element);
    });
});
