import requests

BASE_URL = "https://rahulshettyacademy.com"
API_KEY = "qaclick123"
place_id = None


def test_create_place():

    global place_id

    url = f"{BASE_URL}/maps/api/place/add/json?key={API_KEY}"

    payload = {
        "location": {
            "lat": -38.383494,
            "lng": 33.427362
        },
        "accuracy": 50,
        "name": "Frontline house",
        "phone_number": "(+91) 983 893 3937",
        "address": "29, side layout, cohen 09",
        "types": [
            "shoe park",
            "shop"
        ],
        "website": "http://google.com",
        "language": "French-IN"
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 200

    data = response.json()

    place_id = data["place_id"]

    assert data["status"] == "OK"


def test_get_place():

    url = f"{BASE_URL}/maps/api/place/get/json?key={API_KEY}&place_id={place_id}"

    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Frontline house"
    assert data["language"] == "French-IN"

def test_putUpdateLocation():
    url = f"{BASE_URL}/maps/api/place/update/json?key={API_KEY}"

    payload = {
        "place_id": place_id,
        "address":"100 Lenina street, RU",
        "key": API_KEY
    }
    response = requests.put(url, json=payload)

    data = response.json()

    assert data["msg"] == "Address successfully updated"

def test_deleteLocation():

    url = f"{BASE_URL}/maps/api/place/delete/json?key={API_KEY}"

    payload = {
        "place_id": place_id
    }

    response = requests.delete(url, json=payload)

    print(response.status_code)
    print(response.text)

    data = response.json()

    assert data["status"] == "OK"