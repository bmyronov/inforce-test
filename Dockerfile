FROM python:3.10.8-alpine

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

COPY ./.env .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
