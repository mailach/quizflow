FROM python:3.11
RUN apt-get update && apt-get install -y netcat-openbsd
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN  pip install -r requirements.txt  
EXPOSE 5000
RUN chmod +x /app/init.sh
RUN chmod +x /app/init-dev.sh


ENTRYPOINT ["/bin/sh", "-c", "chmod +x /app/init-dev.sh && /app/init-dev.sh"]  