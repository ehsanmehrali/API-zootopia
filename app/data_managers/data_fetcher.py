
import requests
import os

from dotenv import load_dotenv
from app.data_managers.load_json import write_json_data

load_dotenv()
API_KEY = os.getenv('API_KEY')
print(API_KEY)

def fetch_data(animal_name):
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})

    if response.status_code != requests.codes.ok:
        return "error", f"Error: {response.status_code}"

    animals_info = response.json()
    if not animals_info:
        return "error", "404 Not Found"

    write_json_data(animals_info)
    return "ok", ""



