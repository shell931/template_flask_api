FROM python:3.11
WORKDIR /code
COPY . /code
RUN pip3 install -r requirements.txt
EXPOSE 4000
RUN chmod +x gunicorn_starter.sh
ENTRYPOINT [ "./gunicorn_starter.sh"]
