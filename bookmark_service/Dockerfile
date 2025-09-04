# In bookmark_service/Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# The runserver command will be overridden by docker-compose
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8001"]