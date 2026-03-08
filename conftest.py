import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture
def token():
    response = requests.post(
        f"{BASE_URL}/auth",
        json={
            "username": "admin",
            "password": "password123"
        }
    )

    return response.json()["token"]


@pytest.fixture
def booking_id():

    payload = {
        "firstname": "Max",
        "lastname": "Brownik",
        "totalprice": 11231,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2017-01-01",
            "checkout": "2020-01-01"
        },
        "additionalneeds": "Dinner"
    }

    response = requests.post(
        f"{BASE_URL}/booking",
        json=payload
    )

    return response.json()["bookingid"]