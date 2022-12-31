FROM python:3.10

WORKDIR /project1/app

COPY ./requirements.txt /project1/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /project1/requirements.txt

COPY ./app /project1/app

ENV PYTHONPATH /project1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]