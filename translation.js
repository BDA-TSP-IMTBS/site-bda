// translation.js

document.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    const lang = urlParams.get('lang') || 'fr'; // Langue par défaut : fr

    loadLanguage(lang);
});

function loadLanguage(lang) {
    fetch('/translations.json')
        .then(response => response.json())
        .then(translations => {
            // Remplacer le texte pour chaque élément qui doit être traduit
            document.querySelectorAll('[data-i18n]').forEach(element => {
                const key = element.getAttribute('data-i18n');
                if (translations[lang][key]) {
                    element.textContent = translations[lang][key];
                }
            });

            // Mise à jour de l'URL sans recharger la page
            const url = new URL(window.location);
            url.searchParams.set('lang', lang);
            window.history.pushState({}, '', url);
        })
        .catch(error => console.error('Error loading translations:', error));
}

function switchLanguage(lang) {
    loadLanguage(lang);
}
