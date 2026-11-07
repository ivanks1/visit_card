from django import forms

from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    def __init__(self, *args, language="ru", **kwargs):
        super().__init__(*args, **kwargs)
        errors = {
            "ru": {
                "required": "Это поле обязательно для заполнения.",
                "invalid_email": "Введите корректный адрес электронной почты.",
            },
            "en": {
                "required": "This field is required.",
                "invalid_email": "Enter a valid email address.",
            },
            "kz": {
                "required": "Бұл өрісті толтыру қажет.",
                "invalid_email": "Электрондық пошта мекенжайын дұрыс енгізіңіз.",
            },
        }.get(language, {
            "required": "This field is required.",
            "invalid_email": "Enter a valid email address.",
        })
        for field in self.fields.values():
            field.error_messages["required"] = errors["required"]
        self.fields["email"].error_messages["invalid"] = errors["invalid_email"]

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"autocomplete": "name", "maxlength": 100}),
            "email": forms.EmailInput(attrs={"autocomplete": "email", "maxlength": 254}),
            "message": forms.Textarea(attrs={"rows": 5, "maxlength": 3000}),
        }
