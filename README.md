# BASE TEMPLATE

Service to __SERVICE_SUMMARY__.

## SETUP

### SETUP YOUR VENV

```bash
# linux
python -m venv .venv
source .venv/bin/activate
```

### INSTALL REQUIREMENTS ON YOUR VENV

```bash
pip install --ignore-installed --no-cache-dir -r requirements.txt
```

## RESOURCES

ENDPOINT | METH
--|--
`/v1/package/script-name/` | `POST`


### SETUP DOCKERFILE
```bash
FROM python:3.11
WORKDIR /code
COPY . /code
RUN pip3 install -r requirements.txt
EXPOSE 4000
RUN chmod +x gunicorn_starter.sh
ENTRYPOINT [ "./gunicorn_starter.sh"]
```

### SETUP DOCKE-COMPOSE
```bash
version: '3.7'
services:
  my-awesome-api:
    build:
      context: .
      dockerfile: Dockerfile
    restart: unless-stopped
    container_name: my-awesome-api
    ports:
      - 4000:4000
    environment:
      MI_ENV_VARIABLE: "example"
```

### SETUP GUNICORN
```bash
#!/bin/sh
gunicorn --workers 2 --threads 2 -b 0.0.0.0:4000 main:app
```

### DEPLOY DOCKER CONTAINER
```bash
# to build
docker-compose up --build
# To run with daemon up
docker-compose up -d
```

# ACKNOWLEDGMENTS

Thanks to all Dyner24 team.

---

* Powered by [Carlos Arriero](mailto:desarrollo@dyner24.com) 😎