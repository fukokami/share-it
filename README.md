# share-it
Website supports the create blogs

## To run with virtual environment

```bash
python -m venv env                  #Only first time
source env/bin/activate             #On Windows use `env/Scripts/activate`
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

## SCSS compiler
```bash
python src/manage.py sass-compiler --watch
```

## URL list

### #auth
| Method   | Url                               | Name                                 | Note                    |
| -------- | --------------------------------- | ------------------------------------ | ----------------------- |
| GET      | accounts/signup/                  | account_signup                       |                         |
| GET      | accounts/login/                   | account_login                        |                         |
| GET/POST | accounts/logout/                  | account_logout                       |                         |
| GET      | accounts/password/change/         | account_change_password              |                         |
| GET      | accounts/password/set/            | account_set_password                 | Set password for social |
| GET      | accounts/inactive/                | account_inactive                     |                         |
| GET/POST | accounts/email/                   | account_email                        |                         |
| GET/POST | accounts/confirm-email/           | account_email_verification_sent      |                         |
| GET/POST | accounts/confirm-email/<key>      | account_confirm_email                |                         |
| GET/POST | accounts/password/reset/          | account_reset_password               |                         |
| GET      | accounts/password/reset/done/     | account_reset_password_done          |                         |
| GET/POST | accounts/password/reset/key/<key> | account_reset_password_from_key      |                         |
| GET      | accounts/password/reset/key/done/ | account_reset_password_from_key_done |                         |
| GET      | accounts/social/login/cancelled/  | socialaccount_login_cancelled        |                         |
| GET      | accounts/social/login/error/      | socialaccount_login_error            |                         |
| GET/POST | accounts/social/signup/           | socialaccount_signup                 | Setting username        |
| GET/POST | accounts/social/connections/      | socialaccount_connections            | Crud 3rd party accounts | 
| GET/POST | accounts/facebook/login           | facebook_login                       |                         |
| GET/POST | accounts/github/login             | github_login                         |                         |
| GET/POST | accounts/google/login             | google_login                         |                         |