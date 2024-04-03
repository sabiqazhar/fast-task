
# Fast Task
if you use another .env, setup your env on database.py and before run the migration, you must setup your db env on alembic.ini. this project is under development, but i want improve the app on the future


## Running Tests project

install pdm first

```bash
  pip install --user pdm
```

install pdm dependencies

```bash
  pdm install
```

migrate db for the first time
```bash
  pdm run alembic upgrade head
```

run the app
```bash
  cd app
```
```bash
  pdm run avicorn main:app
```