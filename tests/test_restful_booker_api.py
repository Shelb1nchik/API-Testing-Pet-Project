import requests
from data.booking_data import payload, update_payload, patch_payload

BASE_URL = "https://restful-booker.herokuapp.com"


def test_create_booking():

    response = requests.post(
        f"{BASE_URL}/booking",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["booking"]["firstname"] == payload["firstname"]
    assert data["booking"]["lastname"] == payload["lastname"]
    assert data["booking"]["totalprice"] == payload["totalprice"]
    assert data["booking"]["depositpaid"] == payload["depositpaid"]
    assert data["booking"]["bookingdates"]["checkin"] == payload["bookingdates"]["checkin"]
    assert data["booking"]["bookingdates"]["checkout"] == payload["bookingdates"]["checkout"]
    assert data["booking"]["additionalneeds"] == payload["additionalneeds"]


def test_get_booking(booking_id):

    response = requests.get(
        f"{BASE_URL}/booking/{booking_id}"
    )

    data = response.json()

    assert response.status_code == 200
    assert data["firstname"] == payload["firstname"]
    assert data["lastname"] == payload["lastname"]


def test_put_booking(booking_id, token):

    headers = {
        "Cookie": f"token={token}"
    }

    response = requests.put(
        f"{BASE_URL}/booking/{booking_id}",
        json=update_payload,
        headers=headers
    )

    data = response.json()

    assert response.status_code == 200
    assert data["firstname"] == update_payload["firstname"]


def test_patch_booking(booking_id, token):

    headers = {
        "Cookie": f"token={token}"
    }

    response = requests.patch(
        f"{BASE_URL}/booking/{booking_id}",
        json=patch_payload,
        headers=headers
    )

    data = response.json()

    assert response.status_code == 200
    assert data["firstname"] == patch_payload["firstname"]
    assert data["lastname"] == patch_payload["lastname"]


def test_delete_booking(booking_id, token):

    headers = {
        "Cookie": f"token={token}"
    }

    response = requests.delete(
        f"{BASE_URL}/booking/{booking_id}",
        headers=headers
    )

    assert response.status_code == 201