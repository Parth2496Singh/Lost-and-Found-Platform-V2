FROM python:3.14

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt && \
    python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]