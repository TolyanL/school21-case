# 🟢 School21 Case
Hello programmers 👋🎃!

## Installation:
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
python school21_case/manage.py makemigrations
python school21_case/manage.py migrate
python school21_case/manage.py runserver
```
