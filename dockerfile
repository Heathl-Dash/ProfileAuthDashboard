FROM python:3.12
ENV PYTHONUNBUFFERED=1
WORKDIR /app/
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY manage.py /app/
COPY ./profileAuth /app/profileAuth
COPY ./profileCore /app/profileCore
EXPOSE 8000
RUN python manage.py makemigrations
