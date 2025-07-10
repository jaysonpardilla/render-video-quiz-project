# Use an official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /app/

# Run migrations then start the app using Gunicorn
CMD ["sh", "-c", "python manage.py migrate && python create_superuser.py && gunicorn quizapi.wsgi:application --bind 0.0.0.0:8000"]
