FROM python:3.8
WORKDIR /app
COPY . ./
EXPOSE 3333
ENTRYPOINT [ "python", "./helloworld.py"]