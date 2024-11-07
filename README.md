# 🟢 School21 Case
Hello programmers 👋🎃!

## 📚 Table of contents:
1. [Installation](#installation)
2. [Update to latest stable version](#update)


## Installation
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


## Backup
1. Create backup (static & db)
```bash
python manage.py archive
```
