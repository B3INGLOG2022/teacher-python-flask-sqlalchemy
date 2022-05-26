FROM python:3.7-alpine
WORKDIR /app
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add gcc musl-dev
RUN apk add --update mariadb-dev
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .
ENTRYPOINT [ "flask" , "run" ]
