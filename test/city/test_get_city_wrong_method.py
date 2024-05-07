import requests
from assertpy import assert_that
from setting.endpoint import API_CITY
from setting.general import api_key, max_latency


def test():
    head = {
        "key": api_key
    }
    req = requests.post(API_CITY, headers=head)
    print(req.json())

    #VERIFIKASI
    status_code = req.status_code
    latency = req.elapsed.microseconds
    description = req.json().get("rajaongkir")["status"]["description"]



    #ASSERT
    assert_that(status_code).is_equal_to(400)
    assert_that(latency).is_less_than(max_latency)
    assert_that(description).is_equal_to("Unknown method. Method tidak ditemukan, harap baca dokumentasi dengan baik.")

