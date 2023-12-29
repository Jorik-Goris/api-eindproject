import requests
import json

BASE_URL = "http://127.0.0.1:8000"


def test_get_all_tasks():
    response = requests.get(f"{BASE_URL}/tasks/")
    assert response.status_code == 200


def test_get_specific_task():
    response = requests.get(f"{BASE_URL}/tasks/{1}")
    assert response.status_code == 200


def test_get_specific_task_for_specific_user():
    response = requests.get(f"{BASE_URL}/tasks/user/{1}")
    assert response.status_code == 200


def test_get_specific_tasks_from_specific_cat():
    example_cat = "sports"
    response = requests.get(f"{BASE_URL}/tasks/category/{example_cat}")
    assert response.status_code == 200

