import requests
from assertpy import assert_that
from setting.endpoint import API_COST
from setting.general import api_key, max_latency


def test():
    head = {
        "key": api_key
    }
    payload = {
        "origin": "109",
        "destination": "55",
        "weight": "5000",
        "courier": "jne"
    }
    req = requests.get(API_COST, headers=head, json=payload)
    print(req.json())
    #VERIFIKASI
    status_code = req.status_code
    latency = req.elapsed.microseconds
    description = req.json().get("rajaongkir")["status"]["description"]


    #ASSERT
    assert_that(status_code).is_equal_to(400)
    assert_that(latency).is_less_than(max_latency)
    assert_that(description).is_equal_to("Unknown method. Method tidak ditemukan, harap baca dokumentasi dengan baik.")

