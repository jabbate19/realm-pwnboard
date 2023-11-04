FROM python:3.9.6

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]