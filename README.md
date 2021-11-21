# API_Hero

## 💻 Project

This project is a simple API for registration and control of companies and their employees.
  - Employees are also system users and can belong to more than one company.

Below Screenshot from the browsable API:
![image](/readme_img/main_screen.png?raw=true "Main_Screen")

## 🚀 Technologies

This project was developed with the following tecnologies:
- Python 3.10
- Django 3.2.9
- Django Rest Framework 3.12.4
- Docker

The database used for this application was `postgreSQL`.

## ℹ️ Run the project

- (Local) In the terminal, run:
```
git clone https://github.com/marcocapozzoli/API_Hero.git
docker-compose up --build
```

- Don't forget to run migrations:
```
docker-compose exec web python manage.py migrate
```
- This project was hosted on a heroku server: `https://drf-hero-api.herokuapp.com/v1/`. If you don't want to clone and run locally, you can test it online.

## Tests

- to run the tests:
```
docker-compose exec web pytest

# other options:
docker-compose exec web pytest -x --cov
```
- The tests were divided into three files, models, serializers and views. Where the main purpose was to check requests for endpoints

- Test coverage:
![image](/readme_img/test_coverage.png?raw=true "Test_coverage")

## Endpoints and Features

- List all companies or employees
  - `(GET) /v1/companies/`
  - `(GET) /v1/employees/`
- Create a company or employee:
  - `(POST)/v1/companies/`
  - `(POST)/v1/employees/`
- Show a specific company or employee
  - `(GET) /api/companies/{id}/`
  - `(GET) /api/employees/{id}/`
- Update a specific company or employee
  - `(PUT) /api/companies/{id}/`
  - `(PUT) /api/employees/{id}/`
- Delete a specific company or employee
  - `(DELETE) /api/companies/{id}/`
  - `(DELETE) /api/employees/{id}/`
- It is possible to search for a user by their username
  - `(GET) /api/employees/?username=user1`

- It is also possible to register a company without passing any employee on the payload and add later
![image](/readme_img/create_company.png?raw=true "Create_company")

## 📎 Versioning

1.0.0.0

## 🧔 Authors

* **Marco Capozzoli**: e-mail: marcocapozzoli90@gmail.com

## 📚 Referências
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django](https://www.djangoproject.com/)
