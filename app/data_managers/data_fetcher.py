
import requests

from app.data_managers.load_json import write_json_data


def fetch_data(animal_name):
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    response = requests.get(api_url, headers={'X-Api-Key': 'aEfEpbxZxmntBiqp6e63GA==Hn7E6QgrnQugFEys'})

    if response.status_code != requests.codes.ok or not response.json():
        print(f"Error: 404 Not Found, No animals match '{animal_name}'")
        return None

    animals_info = response.json()
    write_json_data(animals_info)
    return animals_info



