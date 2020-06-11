FROM nikolaik/python-nodejs:python3.8-nodejs10

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt ./

COPY Makefile ./

COPY package.json ./

RUN make install

RUN npm install

COPY . .

RUN make serve-setup

EXPOSE 8000

CMD ["sh", "-c", ". /usr/src/app/venv/bin/activate && make serve"]
