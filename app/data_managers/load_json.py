
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
JSON_FILE_PATH = os.path.join(BASE_DIR, "animals_data", "animals_data.json")


def read_json_data():
    """ Loads a JSON file """
    with open(JSON_FILE_PATH, "r", encoding="utf-8") as handle:
        return json.load(handle)

def write_json_data(animals):
    """ Writes fetched data in json file """
    with open(JSON_FILE_PATH, "w", encoding="utf-8") as handle:
        json.dump(animals, handle)


def main():
    json_data = read_json_data()
    print(json_data)

if __name__ == '__main__':
    main()