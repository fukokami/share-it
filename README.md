# share-it
Website supports the create blogs

## To run with virtual environment

```bash
python -m venv env                  #Only first time
source env/bin/activate             #On Windows use `env\Scripts\activate`
pip install -r requirements.txt
set -a; source .env; set +a
```

## To run with docker
```bash
docker-compose up -d
```

### Helpful command

| Work                  | Command                                                       |
| --------------------- | ------------------------------------------------------------- |
| **Docker**            |                                                               |
| check docker logs     | `docker-compose logs -f`                                      |
| remove data volumes   | `docker-compose down -v`                                      |
| rebuild image         | `docker-compose build <container-name>`                       |
| **Python-Django**     |                                                               |
| python                | `docker-compose run web [command]`                            |
| migrate database      | `docker-compose run web python src/manage.py migrate`         |
| start project         | `docker-compose run web django-admin startproject <name> .`   |
| start app             | `docker-compose run web python src/manage.py startapp <name>` |
| **Database**          |                                                               | 
| postgres command line | `docker-compose exec db psql --username=<user> --dbname=<db>` |
