import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_animals_info(animals):
    """ Prints selected information for each animal. """
    for animal in animals:
        print(f"name: {animal.get('name', 'Unknown')}")

        # Locations
        locations = animal.get("locations", [])
        print("locations:", " ".join(locations))

        # Characteristics
        characteristics = animal.get("characteristics", {})
        for key in ["diet", "type"]:
            if key in characteristics:
                print(f"{key}: {characteristics[key]}")

        print("...........")


def main():
    """ Runs main services such as display animals infos """
    animals_data = load_data('animals_data.json')
    print_animals_info(animals_data)


if __name__ == "__main__":
    main()