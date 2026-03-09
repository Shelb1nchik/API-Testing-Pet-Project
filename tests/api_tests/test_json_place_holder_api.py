import pytest
import requests
BASE_URL = "https://jsonplaceholder.typicode.com"
ID = 1

def test_create_post():
    url = f"{BASE_URL}/posts"

    payload = {
        "title": "QA Pet Project",
        "body": "This is a test post",
        "userId": 1
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 201

    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

def test_get_post():
    url = f"{BASE_URL}/posts/{ID}"

    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == ID
    assert "title" in data

def test_update_post():
    url = f"{BASE_URL}/posts/{ID}"
    payload = {
        "id": ID,
        "title": "Updated QA Post",
        "body": "Updated body",
        "userId": 1
    }

    response = requests.put(url, json=payload)

    assert response.status_code == 200

    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]

def test_delete_post():
    url = f"{BASE_URL}/posts/{ID}"

    response = requests.delete(url)

    # JSONPlaceholder возвращает пустой объект {}
    assert response.status_code == 200
    assert response.text == "{}"