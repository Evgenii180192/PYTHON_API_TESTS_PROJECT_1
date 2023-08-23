"""The module contains methods that are executed before each autotest"""


import pytest
import requests
from loguru import logger
from requests import Timeout

from src.data_requests import URL_LIST_USERS, URL_SINGLE_USER, URL_SINGLE_USER_NOT_FOUND, URL_LIST_RESOURCE, \
    URL_SINGLE_RESOURCE, URL_SINGLE_RESOURCE_NOT_FOUND, URL_CREATE, data_create, URL_UPDATE, data_update, \
    URL_UPDATE_PATCH, data_update_patch, URL_DELETE, URL_REGISTER, data_register, URL_REGISTER_UNSUCCESSFUL, \
    data_register_unsuccessful, URL_LOGIN, data_login, URL_LOGIN_UNSUCCESSFUL, data_login_unsuccessful, \
    URL_DELAYED_RESPONSE
from src.errors import TimeoutResponseError


@pytest.fixture
def request_list_users():
    logger.info("Send request")
    try:
        response = requests.get(url=URL_LIST_USERS, timeout=1)
    except Timeout:
        raise ValueError(TimeoutResponseError.TIMEOUT_Response_ERROR.value)
    return response


@pytest.fixture()
def request_single_user():
    logger.info("Send request")
    try:
        response = requests.get(url=URL_SINGLE_USER, timeout=1)
    except Timeout:
        raise ValueError(TimeoutResponseError.TIMEOUT_Response_ERROR.value)
    return response


@pytest.fixture()
def request_single_user_not_found():
    logger.info("Send request")
    try:
        response = requests.get(url=URL_SINGLE_USER_NOT_FOUND, timeout=1)
    except Timeout:
        raise ValueError(TimeoutResponseError.TIMEOUT_Response_ERROR.value)
    return response


@pytest.fixture()
def request_list_resource():
    logger.info("Send request")
    try:
        response = requests.get(url=URL_LIST_RESOURCE, timeout=1)
    except Timeout:
        raise ValueError(TimeoutResponseError.TIMEOUT_Response_ERROR.value)
    return response


@pytest.fixture()
def request_single_resource():
    logger.info("Send request")
    try:
        response = requests.get(url=URL_SINGLE_RESOURCE, timeout=1)
    except Timeout:
        raise ValueError(TimeoutResponseError.TIMEOUT_Response_ERROR.value)
    return response


@pytest.fixture()
def request_single_resource_not_found():
    logger.info("Send request")
    try:
        response = requests.get(url=URL_SINGLE_RESOURCE_NOT_FOUND, timeout=1)
    except Timeout:
        raise ValueError(TimeoutResponseError.TIMEOUT_Response_ERROR.value)
    return response


@pytest.fixture()
def request_create():
    logger.info("Send request")
    try:
        response = requests.post(url=URL_CREATE, data=data_create, timeout=1)
    except Timeout:
        raise ValueError(TimeoutResponseError.TIMEOUT_Response_ERROR.value)
    return response


@pytest.fixture()
def request_update():
    try:
        logger.info("Send request")
        response = requests.put(url=URL_UPDATE, data=data_update, timeout=1)
    except Timeout:
        raise ValueError(TimeoutResponseError.TIMEOUT_Response_ERROR.value)
    return response


@pytest.fixture()
def request_update_patch():
    try:
        logger.info("Send request")
        response = requests.patch(url=URL_UPDATE_PATCH, data=data_update_patch, timeout=1)
    except Timeout:
        raise ValueError(TimeoutResponseError.TIMEOUT_Response_ERROR.value)
    return response


@pytest.fixture()
def request_delete():
    try:
        logger.info("Send request")
        response = requests.delete(url=URL_DELETE, timeout=1)
    except Timeout:
        raise ValueError(TimeoutResponseError.TIMEOUT_Response_ERROR.value)
    return response


@pytest.fixture()
def request_register():
    try:
        logger.info("Send request")
        response = requests.post(url=URL_REGISTER, data=data_register, timeout=1)
    except Timeout:
        raise ValueError(TimeoutResponseError.TIMEOUT_Response_ERROR.value)
    return response


@pytest.fixture()
def request_register_unsuccessful():
    try:
        logger.info("Send request")
        response = requests.post(url=URL_REGISTER_UNSUCCESSFUL, data=data_register_unsuccessful, timeout=1)
    except Timeout:
        raise ValueError(TimeoutResponseError.TIMEOUT_Response_ERROR.value)
    return response


@pytest.fixture()
def request_login():
    try:
        logger.info("Send request")
        response = requests.post(url=URL_LOGIN, data=data_login, timeout=1)
    except Timeout:
        raise ValueError(TimeoutResponseError.TIMEOUT_Response_ERROR.value)
    return response


@pytest.fixture()
def request_login_unsuccessful():
    try:
        logger.info("Send request")
        response = requests.post(url=URL_LOGIN_UNSUCCESSFUL, data=data_login_unsuccessful, timeout=1)
    except Timeout:
        raise ValueError(TimeoutResponseError.TIMEOUT_Response_ERROR.value)
    return response


@pytest.fixture()
def request_delayed_response():
    try:
        logger.info("Send request")
        response = requests.get(url=URL_DELAYED_RESPONSE, timeout=5)
    except Timeout:
        raise ValueError(TimeoutResponseError.TIMEOUT_Response_ERROR.value)
    return response