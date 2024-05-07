import requests
from assertpy import assert_that
from setting.general import api_key, max_latency


def test():
    head = {
        "key": api_key
    }
    req = requests.get("https://api.rajaongkir.com/starter/cityyy", headers=head)

    #VERIFIKASI
    status_code = req.status_code
    latency = req.elapsed.microseconds



    #ASSERT
    assert_that(status_code).is_equal_to(404)
    assert_that(latency).is_less_than(max_latency)
