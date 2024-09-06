FROM python:3.12

RUN mkdir -p /home/ansible/justbot/bot
WORKDIR /home/ansible/justbot/bot

COPY . /home/ansible/justbot/For_Jenkins
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]