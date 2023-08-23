URL_LIST_USERS = "https://reqres.in/api/users?page=2"

URL_SINGLE_USER = "https://reqres.in/api/users/2"

URL_SINGLE_USER_NOT_FOUND = "https://reqres.in/api/users/23"

URL_LIST_RESOURCE = "https://reqres.in/api/unknown"

URL_SINGLE_RESOURCE = "https://reqres.in/api/unknown/2"

URL_SINGLE_RESOURCE_NOT_FOUND = "https://reqres.in/api/unknown/23"

URL_CREATE = "https://reqres.in/api/users?page=2"

data_create = {
    "name": "morpheus",
    "job": "leader"
}


URL_UPDATE = "https://reqres.in/api/users/2"

data_update = {
    "name": "morpheus",
    "job": "zion resident"
}


URL_UPDATE_PATCH = "https://reqres.in/api/users/2"
data_update_patch = {
    "name": "morpheus",
    "job": "zion resident"
}

URL_DELETE = "https://reqres.in/api/users/2"


URL_REGISTER = "https://reqres.in/api/register"
data_register = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

URL_REGISTER_UNSUCCESSFUL = "https://reqres.in/api/register"
data_register_unsuccessful = {
    "email": "sydney@fife"
}

URL_LOGIN = "https://reqres.in/api/login"
data_login = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

URL_LOGIN_UNSUCCESSFUL = "https://reqres.in/api/login"
data_login_unsuccessful = {
    "email": "peter@klaven"
}

URL_DELAYED_RESPONSE = "https://reqres.in/api/users?delay=3"