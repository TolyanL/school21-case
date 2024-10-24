# 🟢 School21 Case
Hello programmers 👋🎃!

## 📚 Table of contents:
1. [Installation](#installation)
2. [Update to latest stable version](#update)
3. [Project tree](#project-tree)


## Installation
### 1. Clone repo
```bash
git clone https://github.com/TolyanL/school21-case.git
```

### 2. Install requirements
  #### 1. Uv
  ```bash
  uv sync
  ```
  #### 2. Poetry
  ```bash
  poetry shell
  poetry install
  ```

### 2. Run Docker container (development)
```
docker compose -f docker_compose.yaml up -d --build
```

### 3. Run server
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
```

## Project tree
```
├── Dockerfile
├── LICENSE
├── README.md
├── docker-compose.dev.yaml
├── pyproject.toml
├── school21_case
│   ├── home
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── static
│   │   │   ├── css
│   │   │   ├── fonts
│   │   │   ├── img
│   │   │   └── js
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── manage.py
│   ├── media
│   ├── school21_case
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── templates
│       ├── base.html
│       ├── charts
│       │   ├── charts.html
│       │   └── sparkline.html
│       ├── components
│       │   ├── avatars.html
│       │   ├── buttons.html
│       │   ├── font-awesome-icons.html
│       │   ├── gridsystem.html
│       │   ├── notifications.html
│       │   ├── panels.html
│       │   ├── simple-line-icons.html
│       │   ├── sweetalert.html
│       │   └── typography.html
│       ├── forms
│       │   └── forms.html
│       ├── icon-menu.html
│       ├── includes
│       │   ├── main_header.html
│       │   ├── sidebar_1.html
│       │   └── sidebar_2.html
│       ├── index.html
│       ├── maps
│       │   ├── googlemaps.html
│       │   └── jsvectormap.html
│       ├── starter-template.html
│       ├── tables
│       │   ├── datatables.html
│       │   └── tables.html
│       └── widgets.html
└── uv.lock

21 directories, 54 files
```
