FROM python:3

RUN useradd -ms /bin/bash django

USER django

ENV PYTHONUNBUFFERRED 1

WORKDIR /home/django/app

ENV PATH $PATH:/home/django/.local/bin

COPY requirements.txt /home/django/app

RUN pip install -r requirements.txt

COPY . /home/django/app

CMD ["python" ,"manage.py", "runserver", "0.0.0.0:8000"]