FROM python:3.9-slim

# Keep these for better logging and performance
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create workdir and copy files
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/

# Run server directly (no static collection)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]