FROM python:3.9.1

WORKDIR /usr/src/recoart_wiki_api

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]



