import json


def elements_to_json(arr):
    return list(element.to_json() for element in arr)


def list_to_json(arr):
    return json.dumps(elements_to_json(arr))

