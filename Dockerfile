FROM ubuntu:19.04
LABEL maintainer="helton.doria@gmail.com"
RUN apt-get update && apt-get install -y python \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
RUN apt-get install -y --no-install-recommends python3-pip python3-dev build-essential git
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
