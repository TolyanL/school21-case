# 🟢 School21 Case
Hello programmers 👋🎃!

## 📚 Table of contents:
1. [Installation](#installation)
2. [Update to latest stable version](#update)


## 📦 Installation
1. Clone repo
```bash
git clone https://github.com/TolyanL/school21-case.git
```

2. Run Docker container (development)
```
docker compose -f docker_compose.yaml up -d --build
```

3. Run server
```bash
cd school21_case
```
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


## ⬇️ Update
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
