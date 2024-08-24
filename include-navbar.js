document.addEventListener("DOMContentLoaded", function () {
    fetch("/navbar.html")
        .then(response => response.text())
        .then(data => {
            document.getElementById("navbar-container").innerHTML = data;
            
            // Maintenant que le navbar est inclus, nous pouvons ajouter les événements du menu burger
            addMenuBurgerFunctionality();
        });
});
