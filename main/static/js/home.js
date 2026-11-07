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
        const option = event.target.closest('a.lang-option');
        if (!option || !['ru', 'en', 'kz'].includes(option.dataset.lang)) return;
        const language = option.dataset.lang;
        document.cookie = `user_language=${language}; max-age=604800; path=/; samesite=lax`;
    });

    document.addEventListener('click', (event) => {
        if (!(event.target instanceof Node)) return;
        if (!button.contains(event.target) && !menu.contains(event.target)) {
            menu.hidden = true;
            button.setAttribute('aria-expanded', 'false');
        }
    });

    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && !menu.hidden) {
            menu.hidden = true;
            button.setAttribute('aria-expanded', 'false');
            button.focus();
        }
    });
});
