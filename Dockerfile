FROM python:3.5

COPY . /code/
WORKDIR /code/

RUN pip install -r requirements.txt
CMD python main.py

