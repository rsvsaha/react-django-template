# syntax=docker/dockerfile:1
FROM python:3.8-slim
WORKDIR /app
EXPOSE 8000
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /app
CMD ["python3","manage.py", "runserver", "0.0.0.0:8000"]