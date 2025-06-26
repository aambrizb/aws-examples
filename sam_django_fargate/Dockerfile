FROM --platform=linux/amd64 python:3.13-slim

COPY . /opt/app

WORKDIR /opt/app

RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py makemigrations app
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "sam_django_fargate.wsgi"]
