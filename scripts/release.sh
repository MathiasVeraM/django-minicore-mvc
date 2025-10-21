#!/usr/bin/env bash
set -e

echo "==== Running migrations ===="
python manage.py migrate

echo "==== Collecting static files ===="
python manage.py collectstatic --noinput

echo "==== Creating superuser if env vars set ===="
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
  python - <<'PY'
import os
from django.contrib.auth import get_user_model
User = get_user_model()
u = os.environ.get('DJANGO_SUPERUSER_USERNAME')
e = os.environ.get('DJANGO_SUPERUSER_EMAIL') or ''
p = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
if u and p and not User.objects.filter(username=u).exists():
    User.objects.create_superuser(u, e, p)
print("Superuser created or already exists.")
PY
else
  echo "Superuser environment variables not set — skipping."
fi

echo "==== Release script finished ===="
