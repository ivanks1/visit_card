document.addEventListener('DOMContentLoaded', () => {
    const button = document.querySelector('.language');
    const menu = document.querySelector('.lang-choice');
    if (!button || !menu) return;

    button.addEventListener('click', () => {
        menu.hidden = !menu.hidden;
        button.setAttribute('aria-expanded', String(!menu.hidden));
    });

    menu.addEventListener('click', (event) => {
        if (!(event.target instanceof Element)) return;
        const option = event.target.closest('.lang-option');
        if (!option) return;

        const language = option.dataset.lang;
        if (!['ru', 'en', 'kz'].includes(language)) return;

        document.cookie = `user_language=${language}; max-age=604800; path=/; samesite=lax`;
        window.location.assign(`/${language}/`);
    });

    document.addEventListener('click', (event) => {
        if (!(event.target instanceof Node)) return;
        if (!button.contains(event.target) && !menu.contains(event.target)) {
            menu.hidden = true;
            button.setAttribute('aria-expanded', 'false');
        }
    });
});

