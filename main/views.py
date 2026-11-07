from django.contrib import messages
from django.shortcuts import redirect, render

from backoffice.forms import ContactMessageForm


LANGUAGES = {
    "ru": {
        "name": "Русский",
        "nav_about": "Обо мне",
        "nav_services": "Услуги",
        "nav_process": "Процесс",
        "nav_contact": "Контакты",
        "eyebrow": "Веб-разработка · Дизайн · Запуск",
        "headline": "Сайты, которые",
        "headline_accent": "работают на вас",
        "intro": "Создаю быстрые, понятные и запоминающиеся сайты для бизнеса и личных проектов — от первой идеи до публикации.",
        "primary_action": "Обсудить проект",
        "secondary_action": "Мои услуги",
        "availability": "Открыт к новым проектам",
        "about_label": "Обо мне",
        "about_title": "Ваш проект заслуживает сильного присутствия в интернете.",
        "about_text": "Apex Web — разработка сайтов с вниманием к деталям и к вашим задачам. Без лишней сложности: продумываем структуру, создаём удобный дизайн и доводим сайт до готового результата.",
        "services_label": "Чем могу помочь",
        "services_title": "Всё необходимое для вашего сайта",
        "services": [
            ("Сайты-визитки", "Современная страница, которая рассказывает о вас и помогает клиентам связаться."),
            ("Сайты для бизнеса", "Продуманные страницы услуг и продуктов с удобной навигацией и ясными призывами к действию."),
            ("Редизайн и поддержка", "Обновление существующего сайта, адаптация под мобильные устройства и регулярные улучшения."),
        ],
        "process_label": "Как мы работаем",
        "process_title": "От задачи до готового сайта",
        "steps": [
            ("01", "Знакомство", "Обсуждаем вашу задачу, аудиторию и желаемый результат."),
            ("02", "План и дизайн", "Согласуем структуру и визуальное направление до начала разработки."),
            ("03", "Разработка", "Собираю адаптивный сайт и проверяю его на разных устройствах."),
            ("04", "Запуск", "Публикуем готовый проект и передаём вам все необходимые материалы."),
        ],
        "contact_label": "Есть идея?",
        "contact_title": "Давайте обсудим ваш проект",
        "contact_text": "Расскажите, что хотите создать. Я свяжусь с вами, чтобы обсудить задачу и следующие шаги.",
        "form_name": "Ваше имя",
        "form_email": "Электронная почта",
        "form_message": "Коротко о проекте",
        "form_submit": "Отправить сообщение",
        "form_note": "Ваши данные используются только для ответа на обращение.",
        "sent": "Спасибо! Сообщение отправлено. Я свяжусь с вами в ближайшее время.",
        "footer": "Создаю сайты с вниманием к людям и деталям.",
        "language_title": "Выберите язык",
    },
    "en": {
        "name": "English",
        "nav_about": "About",
        "nav_services": "Services",
        "nav_process": "Process",
        "nav_contact": "Contact",
        "eyebrow": "Web development · Design · Launch",
        "headline": "Websites that",
        "headline_accent": "work for you",
        "intro": "I build fast, thoughtful websites for businesses and personal projects — from the first idea to launch.",
        "primary_action": "Let's talk",
        "secondary_action": "Explore services",
        "availability": "Available for new projects",
        "about_label": "About",
        "about_title": "Your project deserves a strong online presence.",
        "about_text": "Apex Web creates websites with care for the details and your goals. No unnecessary complexity: we plan the structure, craft a clear design, and bring your website to life.",
        "services_label": "What I do",
        "services_title": "Everything your website needs",
        "services": [
            ("Personal websites", "A modern page that tells your story and makes it easy for clients to reach you."),
            ("Business websites", "Thoughtful service and product pages with clear navigation and calls to action."),
            ("Redesign & support", "Refresh your existing website, make it mobile-friendly, and keep improving it."),
        ],
        "process_label": "How it works",
        "process_title": "From brief to launch",
        "steps": [
            ("01", "Discovery", "We discuss your goals, audience, and what success looks like."),
            ("02", "Plan & design", "We agree on the structure and visual direction before development."),
            ("03", "Development", "I build a responsive website and test it across devices."),
            ("04", "Launch", "We publish your finished project and hand over everything you need."),
        ],
        "contact_label": "Have an idea?",
        "contact_title": "Let's talk about your project",
        "contact_text": "Tell me a little about what you'd like to build. I'll get back to you to discuss the details and next steps.",
        "form_name": "Your name",
        "form_email": "Email address",
        "form_message": "A little about your project",
        "form_submit": "Send a message",
        "form_note": "Your details will only be used to reply to your message.",
        "sent": "Thanks! Your message has been sent. I'll be in touch soon.",
        "footer": "Thoughtful websites, made for people.",
        "language_title": "Choose a language",
    },
    "kz": {
        "name": "Қазақша",
        "nav_about": "Мен туралы",
        "nav_services": "Қызметтер",
        "nav_process": "Жұмыс барысы",
        "nav_contact": "Байланыс",
        "eyebrow": "Веб-әзірлеу · Дизайн · Іске қосу",
        "headline": "Сізге пайда әкелетін",
        "headline_accent": "сайттар жасаймын",
        "intro": "Бизнес пен жеке жобаларға арналған жылдам әрі есте қаларлық сайттарды алғашқы идеядан іске қосуға дейін жасаймын.",
        "primary_action": "Жобаңызды талқылайық",
        "secondary_action": "Қызметтер",
        "availability": "Жаңа жобаларға ашықпын",
        "about_label": "Мен туралы",
        "about_title": "Жобаңыз интернетте лайықты көрініске ие болсын.",
        "about_text": "Apex Web — егжей-тегжей мен сіздің мақсатыңызға мән беріп сайт әзірлеу. Артық күрделіліксіз: құрылымды ойластырамыз, ыңғайлы дизайн жасап, сайтты толық іске қосамыз.",
        "services_label": "Қалай көмектесемін",
        "services_title": "Сайтыңызға қажет нәрсенің бәрі",
        "services": [
            ("Визитка-сайттар", "Өзіңіз туралы айтып, клиенттерге сізбен байланысуға көмектесетін заманауи бет."),
            ("Бизнес-сайттар", "Түсінікті навигациясы мен нақты әрекетке шақыруы бар қызмет және өнім беттері."),
            ("Жаңарту және қолдау", "Сайтыңызды жаңарту, мобильді құрылғыларға бейімдеу және үнемі жетілдіру."),
        ],
        "process_label": "Жұмыс тәртібі",
        "process_title": "Міндеттен дайын сайтқа дейін",
        "steps": [
            ("01", "Танысу", "Мақсатыңызды, аудиторияңызды және күткен нәтижеңізді талқылаймыз."),
            ("02", "Жоспар және дизайн", "Әзірлеуді бастамас бұрын құрылым мен дизайн бағытын келісеміз."),
            ("03", "Әзірлеу", "Бейімделетін сайт жасап, оны түрлі құрылғыларда тексеремін."),
            ("04", "Іске қосу", "Дайын жобаны жариялап, қажет материалдардың бәрін тапсырамын."),
        ],
        "contact_label": "Идеяңыз бар ма?",
        "contact_title": "Жобаңызды бірге талқылайық",
        "contact_text": "Не жасағыңыз келетінін қысқаша жазыңыз. Міндет пен келесі қадамдарды талқылау үшін хабарласамын.",
        "form_name": "Атыңыз",
        "form_email": "Электрондық пошта",
        "form_message": "Жобаңыз туралы қысқаша",
        "form_submit": "Хабарлама жіберу",
        "form_note": "Деректеріңіз тек хабарламаңызға жауап беру үшін қолданылады.",
        "sent": "Рақмет! Хабарламаңыз жіберілді. Жақын арада хабарласамын.",
        "footer": "Адамдар мен егжей-тегжейге мән беріп жасалған сайттар.",
        "language_title": "Тілді таңдаңыз",
    },
}


def home(request, language=None):
    if language is None:
        language = request.COOKIES.get("user_language", "ru")
        if language not in LANGUAGES:
            language = "ru"
        return redirect(f"/{language}/")

    if language not in LANGUAGES:
        return redirect("home")

    content = LANGUAGES[language]
    form_data = request.POST if request.method == "POST" else None
    form = ContactMessageForm(form_data, language=language)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, content["sent"])
            return redirect(f"/{language}/#contact")

    context = {
        **content,
        "language": language,
        "languages": [
            (code, values["name"])
            for code, values in LANGUAGES.items()
        ],
        "form": form,
    }
    return render(request, "home.html", context)


def page_not_found(request, unknown=""):
    return render(request, "404.html", {"unknown": unknown}, status=404)
