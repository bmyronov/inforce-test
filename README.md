# INFORCE TEST PROJECT

Simple API to vote for the menu before leaving for lunch.

- Restaurants can create account, login and add their menu.
- Restaurants can see only their own menus.
- Employees can create account, login and add vote for a menu.

## Requirements

- Python 3.6
- Django 3.1
- Django REST Framework

## Installation

First, you need to clone git repository.

```
git clone https://github.com/bmyronov/inforce-test.git
```

Then create `.env` file. **Don't forget to change the fields bellow**

```
SECRET_KEY='your_sercret_key'
DB_ENGINE=django.db.backends.postgresql_psycopg2
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
TIMEZONE=Europe/Kiev # Ukrainian TZ
```

Next you need to change `docker-compose.yml`.

```
...
services:
  postgres:
    environment:
        POSTGRES_USER: "your_db_user"
        POSTGRES_PASSWORD: "your_password"
...
```

After that you need to build and start our docker containers.

```
docker compose up -d
docker exec -it postgres createdb -U your_db_user your_db_name
```

## Structure

In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have:

- `api/auth/` authentication endpoints
- `api/menu/` menu endpoints
- `api/vote/` vote endpoints

| Endpoint                  | CRUD Method | Result                                                                                                              |
| ------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------- |
| `api/auth/restaurant/`    | POST        | Creates restaurant account                                                                                          |
| `api/auth/employee/`      | POST        | Creates employee account                                                                                            |
| `api/auth/login/`         | POST        | Allows to obtain JWT token                                                                                          |
| `api/auth/token/refresh/` | POST        | Allows to refresh JWT token                                                                                         |
| `api/auth/token/verify/`  | POST        | Allows to verify JWT token                                                                                          |
| `api/menu/`               | POST        | Allows to create menu. Being authenticated as Restaurant is needed.                                                 |
| `api/menu/`               | GET         | Allows to get today's menus. Employees can see all menus available today. Restaurants can only see their own menus. |
| `api/menu/:id`            | GET         | Allows to get menu with a specific id.                                                                              |
| `api/menu/:id`            | DELETE      | Allows to delete menu with a specific id.                                                                           |
| `api/vote/`               | POST        | Allows to vote for a spicific menu.                                                                                 |
| `api/vote/`               | GET         | Allows to get results of today's votes.                                                                             |

## Usage

We can test the API using [curl](https://curl.haxx.se/) or [httpie](https://github.com/jakubroztocil/httpie#installation), or we can use [Postman](https://www.postman.com/)

To create a restaurant account we can use `api/auth/restaurant/` endpoint. Method `POST`.

```json
{
  "restaurant_name": "Pizza Hub",
  "email": "example@email.com",
  "password": "some_p@ssword"
}
```

To create an employee account we can use `api/auth/employee/` endpoint. Method `POST`.

```json
{
  "email": "example@email.com",
  "password": "some_p@ssword"
}
```

If you want to add menu you need to login as restaurant. To do that you need to acces `api/auth/login/`, Method `POST`.

```json
{
  "email": "example@email.com",
  "password": "some_p@ssword"
}
```

To add a menu you need access `api/menu/`. Method `POST`.

```json
{
    "name":"Pizza Hub Menu", 
    "meal": [
    {
        "name": "Chicken Soup",
        "description": "Chicken Soup, has an eligible taste of chicken!",
        "price": 60,
        "type": "soup"
    },
    {
        "name": "Pizza",
        "description": "Pizza peperony.",
        "price": 160,
        "type": "main"
    }
    ]
}
```

- `name` name of the menu
- `meal` some meal in menu. Has such atributes:
  - `name` name of the meal
  - `description` description of the meal
  - `price` price of the meal
  - `type` type of the meal

`type` can have such values:

- `drink`
- `breacfast`
- `dessert`
- `main`
- `soup`
- `salad`
- `alcohol`

To vote for the menu you need to be logged in as Employee.
Use `api/vote/`. Method `POST`.

```json
{
  "menu": 1
}
```

`menu` is menu_id value. Menu id you can find in `api/menu/`. Method `GET`. **You can vote only once a day!**

To check the result of the vote you can with `api/vote/`. Method `GET`.

## Versioning

You can change versioning inside `api_crud/settings.py`

```python
REST_FRAMEWORK = {
    ...
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.AcceptHeaderVersioning',
    'DEFAULT_VERSION': '1.0',
    'ALLOWED_VERSIONS': ('1.0', '2.0'),
    'VERSION_PARAM': 'version',
}
```
