# 🟢 School21 Case
Hello programmers 👋🎃!

## 📚 Table of contents:
1. [Installation (via Makefile)](#installation-via-makefile)
2. [Installation (Manual)](#installation-manual)
3. [Makefile functions](#makefile-functions)
4. [Update to latest stable version](#update)
5. [Make backups](#backup)


## Installation (via Makefile)
### 1. Clone repo
```bash
git clone https://github.com/TolyanL/school21-case.git
```

### 2. Run Makefile
```bash
make launch
```
This will install all requirements and will automatically start the server see [Makefile functions](#makefile-functions) for more information.

### 3. Create admin
```bash
python school21_case/manage.py createsuperuser
```

### 4. Create interests


## Installation (Manual)
### 1. Clone repo
```bash
git clone https://github.com/TolyanL/school21-case.git
```

### 2. Install requirements
  #### Uv
  ```bash
  uv sync
  source .venv/bin/activate
  ```
  #### Poetry
  ```bash
  poetry shell
  poetry install
  ```
  #### Pip
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  ```

### 3. Run Docker container (development)
```
docker compose -f docker-compose.dev.yaml up -d --build
```

### 4. Run server
```bash
cd school21_case
```
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### 5. Create admin
```bash
python school21_case/manage.py createsuperuser
```

### 6. Create interests


## Makefile functions
| Function | Description |
| ------ | ------ |
| run | Start docker compose & run server |
| launch | First project launch (install requirement, start docker and server, and make migrations) |
| backup | Do database and static files backup |
|  |  |
| install | Install requirements |
| db | Starts database |
| db_down | Downs database |
| migrate | Create migrations and apply they |


## Update
1. Switch to `main` branch
```bash
git checkout main
```

2. Pull latest changes
```bash
git pull
```

3. Make migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## Backup
Create backup (static & db)

### Via Makefile
```bash
make backup
```

### Manual
```bash
mkdir backup
```
```bash
cd school21_case
python manage.py archive
```
