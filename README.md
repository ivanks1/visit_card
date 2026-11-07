# Apex Web

A trilingual web-development portfolio and contact page built with Django. Contact
form submissions are saved in the database and can be reviewed in the Django admin.

## Run locally

```powershell
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`. The language selector supports Russian, English,
and Kazakh; the selection is remembered in a browser cookie.

To review contact requests, create an administrator account with
`python manage.py createsuperuser` and open `http://127.0.0.1:8000/admin/`.

## Configuration

Set `DJANGO_SECRET_KEY` to a private, randomly generated value before deployment.
Set `DJANGO_DEBUG=false` and provide a comma-separated `DJANGO_ALLOWED_HOSTS` list
for the production host names. Run `python manage.py collectstatic` when deploying.
