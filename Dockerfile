
FROM python:3.9

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "-m" , "uvicorn", "main:app", "--reload","--host", "0.0.0.0", "--port", "10000"]
