function addMenuBurgerFunctionality() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navUl = document.querySelector('nav ul');

    menuToggle.addEventListener('click', function() {
        navUl.classList.toggle('active');
    });

    document.querySelectorAll('nav ul li > a').forEach(function(element) {
        element.addEventListener('click', function(e) {
            const nextElement = this.nextElementSibling;
            if (nextElement && nextElement.classList.contains('dropdown')) {
                e.preventDefault();
                nextElement.classList.toggle('active');
            }
        });
    });
}
