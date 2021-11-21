# API_Hero

## 💻 Project

This project is a simple API for register a task.
- It has a token authentication system.
- Only authenticated users can use the API.
- The user must be able to register new tasks, and edit or delete only their own.
- It has a registration screen (optional, if you don't want to use the admin or shell to create a user)

Below Screenshot from the browsable API:
![image](/readme_img/main_screen.png?raw=true "Main_Screen")

## 🚀 Technologies

This project was developed with the following tecnologies:
- Python 3.10
- Django 3.2.9
- Django Rest Framework 3.12.4

The reason for choosing Django and Django Rest Framework was the practicality and productivity for the creation of REST API's, besides particularly liking these tools. 🥰

The database used for this application was `sqlite3`. Because it is already installed and configured with Django, it makes development a lot easier.

## ℹ️ Run the project**

- In the terminal, run
```
git clone https://github.com/marcocapozzoli/API_Hero.git
docker-compose up --build
```

- to run the tests:
```
docker-compose exec web pytest

# ohter options:
docker-compose exec web pytest -x --cov
```

- Don't forget to run migrations:
```
docker-compose exec web python manage.py migrate
```

**3. In operation**
  
Example of creating a task (with Postman):
  
![image](/readme_img/postman_post_api-todolist.png?raw=true "postman_post_api-todolist")

Update a task (with browsable API)
![image](/readme_img/drf_put_api_todolist_id.png?raw=true "drf_put_api-todolist_id")

If the user tries to update or delete a task that he did not create himself, it will not succeed and will display an error message.
![image](/readme_img/drf_put_api_todolist_id_response_error.png?raw=true "drf_put_api-todolist_response_error_id")
![image](/readme_img/drf_delete_api_todolist_id_response_error.png?raw=true "drf_delete_api-todolist_response_error_id")

The API has ordering by delivery date and searching by username. To access this resource, pass this information by parameter.
```
/api/todolist/?ordering=date&search=marco
```

## Endpoints and Features

- Register:
  - `(POST)/signup`
- Get token for API access
  - `(POST)/api/token`
- List all task
  - `(GET) /api/todolist/`
- Create new task
  - `(POST) /api/todolist/`
- Show an specific task
  - `(GET) /api/todolist/{id}/`
- Update a specific task
  - `(PUT) /api/todolist/{id}/`
  - `(PATCH) /api/todolist/{id}/`
- Delete an specific task
  - `(DELETE) /api/todolist/{id}/`

👀 For more information about endpoints, see the documentation on endpoint `(GET)/api/doc/`

## 📎 Versioning

1.0.0.0

## 🧔 Authors

* **Marco Capozzoli**: @marcocapozzoli (https://github.com/marcocapozzoli)

## 📚 Referências
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django](https://www.djangoproject.com/)