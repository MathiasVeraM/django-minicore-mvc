web: gunicorn minicore.wsgi

# línea opcional para crear superuser automáticamente (ver más abajo)
release: python manage.py migrate && python manage.py collectstatic --noinput && python manage.py shell -c "from django.contrib.auth import get_user_model, os; User=get_user_model(); import os; \
u=os.environ.get('DJANGO_SUPERUSER_USERNAME'); e=os.environ.get('DJANGO_SUPERUSER_EMAIL'); p=os.environ.get('DJANGO_SUPERUSER_PASSWORD'); \
if u and p and not User.objects.filter(username=u).exists(): User.objects.create_superuser(u,e,p)"
