from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import ContactMessage


class ContactPageTests(TestCase):
    def test_root_redirects_to_saved_language(self):
        self.client.cookies["user_language"] = "en"
        response = self.client.get("/")
        self.assertRedirects(response, "/en/", fetch_redirect_response=False)

    def test_home_page_renders_in_each_language(self):
        headings = {
            "ru": "работают на вас",
            "en": "work for you",
            "kz": "сайттар жасаймын",
        }
        for language, heading in headings.items():
            with self.subTest(language=language):
                response = self.client.get(reverse(f"home_{language}"))
                self.assertEqual(response.status_code, 200)
                html_language = "kk" if language == "kz" else language
                self.assertIn(f'<html lang="{html_language}">', response.content.decode())
                self.assertContains(response, heading)

    def test_contact_form_saves_message(self):
        response = self.client.post(
            reverse("home_en"),
            {
                "name": "Alex",
                "email": "alex@example.com",
                "message": "I need a new website.",
            },
        )
        self.assertRedirects(response, "/en/#contact", fetch_redirect_response=False)
        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertEqual(ContactMessage.objects.get().email, "alex@example.com")

    def test_contact_form_rejects_invalid_email(self):
        response = self.client.post(
            reverse("home_ru"),
            {"name": "Alex", "email": "not-an-email", "message": "Hello"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["form"].errors["email"])
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_contact_form_shows_required_errors_for_empty_submission(self):
        response = self.client.post(reverse("home_kz"), {})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["form"].errors), 3)
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_unknown_url_returns_not_found(self):
        response = self.client.get("/this/page/does/not/exist/")
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "Page not found", status_code=404)

    def test_admin_can_review_contact_messages(self):
        ContactMessage.objects.create(
            name="Alex",
            email="alex@example.com",
            message="Please contact me.",
        )
        admin = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="test-password",
        )
        self.client.force_login(admin)
        response = self.client.get(reverse("admin:backoffice_contactmessage_changelist"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "alex@example.com")
