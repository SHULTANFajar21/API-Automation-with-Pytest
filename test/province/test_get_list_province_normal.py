import requests
from assertpy import assert_that
from jsonschema import validate as validate_json_schema
from jsonschemas.schema_province import schema_list_province_normal
from setting.endpoint import API_PROVINCE
from setting.general import api_key, max_latency


def test():
    head = {
        "key": api_key
    }
    req = requests.get(API_PROVINCE, headers=head)

    #VERIFIKASI
    status_code = req.status_code
    latency = req.elapsed.microseconds
    description = req.json().get("rajaongkir")["status"]["description"]
    result = req.json().get("rajaongkir")["results"]

    #ASSERT
    assert_that(status_code).is_equal_to(200)
    assert_that(latency).is_less_than(max_latency)
    assert_that(description).is_equal_to("OK")
    assert_that(result).is_type_of(list)
    assert_that(result).is_not_none()
    validate_json_schema(instance=req.json(), schema=schema_list_province_normal)