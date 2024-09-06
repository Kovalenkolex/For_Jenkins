FROM python:3.12

RUN mkdir -p /home/ansible/justbot
WORKDIR /home/ansible/justbot

COPY . /home/ansible/justbot
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]