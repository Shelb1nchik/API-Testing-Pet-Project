import requests
import pytest
BASE_URL = "https://restful-booker.herokuapp.com"

payload = {
     "firstname" : "Max",
     "lastname" : "Brownik",
     "totalprice" : 11231,
     "depositpaid" : True,
     "bookingdates" : {
         "checkin" : "2017-01-01",
         "checkout" : "2020-01-01"
     },
    "additionalneeds" : "Dinner"
}

def test_token():
    global token
    url = f"{BASE_URL}/auth"

    body = {
        "username" : "admin",
        "password" : "password123"
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, json=body, headers=headers)

    data = response.json()
    token = data["token"]
    assert response.status_code == 200
    assert data["token"] != ""

def test_create_booking():
    global id
    url = f"{BASE_URL}/booking"

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 200

    data = response.json()
    id = data["bookingid"]

    assert data["booking"]["firstname"] == payload["firstname"]
    assert data["booking"]["lastname"] == payload["lastname"]
    assert data["booking"]["totalprice"] == payload["totalprice"]
    assert data["booking"]["depositpaid"] == payload["depositpaid"]
    assert data["booking"]["bookingdates"]["checkin"] == payload["bookingdates"]["checkin"]
    assert data["booking"]["bookingdates"]["checkout"] == payload["bookingdates"]["checkout"]
    assert data["booking"]["additionalneeds"] == payload["additionalneeds"]

def test_get_booking():
    url = f"{BASE_URL}/booking/{id}"

    headers = {
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    assert response.status_code == 200
    assert data["firstname"] == payload["firstname"]
    assert data["lastname"] == payload["lastname"]
    assert data["totalprice"] == payload["totalprice"]
    assert data["depositpaid"] == payload["depositpaid"]
    assert data["bookingdates"]["checkin"] == payload["bookingdates"]["checkin"]
    assert data["bookingdates"]["checkout"] == payload["bookingdates"]["checkout"]
    assert data["additionalneeds"] == payload["additionalneeds"]

def test_put_booking():
    url = f"{BASE_URL}/booking/{id}"

    changing = {
        "firstname" : "Maxon123098",
        "lastname" : "Grey",
        "totalprice" : 111234,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2017-01-01",
            "checkout" : "2020-01-01"
        },
        "additionalneeds" : "Dinner and breakfast"
    }

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Cookie': f"token={token}"
    }

    response = requests.put(url, json=changing, headers=headers)
    data = response.json()

    assert response.status_code == 200
    assert data["firstname"] == changing["firstname"]

def test_patch_booking():
    url = f"{BASE_URL}/booking/{id}"

    changing = {
        "firstname": "Michael",
        "lastname": "Shark",
    }

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Cookie': f"token={token}"
    }

    response = requests.patch(url, json=changing, headers=headers)
    data = response.json()

    assert response.status_code == 200
    assert data["firstname"] == changing["firstname"]
    assert data["lastname"] == changing["lastname"]

def test_delete_booking():
    url = f"{BASE_URL}/booking/{id}"

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Cookie': f"token={token}"
    }

    response = requests.delete(url, headers=headers)

    assert response.status_code == 201