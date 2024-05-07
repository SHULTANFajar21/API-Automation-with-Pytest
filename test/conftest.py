import pytest
import json


@pytest.fixture(scope='function', autouse=True)
def hook(request):
    # print("\nbefore test")
    get_error = request.session.testsfailed

    yield
    # print("after test")
    test_result = request.session.testsfailed - get_error

    if test_result == 0:
        with open('test_bag.json', 'r') as file:
            data = json.load(file)
            data['success'].append(1)
            with open('test_bag.json', 'w') as file:
                json.dump(data, file, indent=4)

    else:
        with open('test_bag.json', 'r') as file:
            data = json.load(file)
            data['failed'].append(1)
            with open('test_bag.json', 'w') as file:
                json.dump(data, file, indent=4)
                


@pytest.fixture(scope='session', autouse=True)
def suite(request):
    # print("\nbefore all)
    json_temp = {
        "other": [],
        "failed": [],
        "success": []
    }
    jsonString = json.dumps(json_temp)
    jsonFile =open("test_bag.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
    yield
    # print("after all")
