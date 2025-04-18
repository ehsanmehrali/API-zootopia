import json

def load_html(file_path):
    """ Loads an HTML file """
    with open(file_path, "r") as handle:
        return handle.read()

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def animals_info(animals):
    """
    It creates a string of desired information for each animal.
    :param animals: A list of animals infos
    :return: A string
    """

    output = "" # define an empty string
    for animal in animals:
        output += f"name: {animal.get('name', 'Unknown')}\n"

        # Locations
        locations = animal.get("locations", [])
        all_location = ' '.join(locations)
        output += f"locations: {all_location}\n"

        # Characteristics
        characteristics = animal.get("characteristics", {})
        for key in ["diet", "type"]:
            if key in characteristics:
                output += f"{key}: {characteristics[key]}\n"

    return output


def main():
    """ Runs main services such as display animals infos """
    animals_data = load_data('animals_data.json')
    html_content = load_html('animals_template.html')
    specifications = animals_info(animals_data)
    print(specifications)


if __name__ == "__main__":
    main()