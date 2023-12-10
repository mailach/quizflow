FROM python:3.11
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN  pip install -r requirements.txt  
EXPOSE 5000
RUN chmod +x /app/init.sh
RUN chmod +x /app/init-dev.sh


ENTRYPOINT ["/app/init-dev.sh"]  