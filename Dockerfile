FROM ubuntu:17.10
MAINTAINER Helton Costa
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential git
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "run.py"]

# docker build -t contato-service .
#
# For Development Container
# docker run -dt --name=contato-service -v $PWD:/app -p 5000:5000 -e 'WORK_ENV=DEV' contato-service
#
# For Production Container
# docker run -dt --restart=always --name=contato-service -p 5000:5000 -e 'WORK_ENV=PROD' contato-service
#
# Remove the container
# docker rm -f contato-service

# docker logs --follow contato-service
# docker exec -it contato-service bash