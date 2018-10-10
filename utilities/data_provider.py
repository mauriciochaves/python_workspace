import json
import os


def test_data_provider():
    try:
        abs_path = os.path.dirname(os.path.realpath(__file__)) + "/data.json"
        with open(abs_path, "r") as data_provider:
            read_json_file = json.load(data_provider)
        return read_json_file
    except:
        raise Exception("No JSON file found!")
