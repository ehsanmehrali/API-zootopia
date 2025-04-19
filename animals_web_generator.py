import json

HTML_FILE_PATH = "animals_template.html"
JSON_FILE_PATH = "animals_data.json"

def load_html(html_file_path):
    """ Loads an HTML file. """
    with open(html_file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def write_html(html_file_path, content):
    """ Writes new content in HTML file. """
    with open(html_file_path, "w", encoding="utf-8") as handle:
        handle.write(content)


def load_data(json_file_path):
    """ Loads a JSON file """
    with open(json_file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def animals_info(animals):
    """
    It creates a string of desired information from all animal.
    :param animals: A list of animals infos
    :return: A string of animals info
    """

    output = "" # define an empty string
    for animal in animals:
        output += '<li class="cards__item">'
        output += f"<div class='card__title'>name: {animal.get('name', 'Unknown')}</div><br/>\n"

        output += "<p class='card__text'>"
        # Locations
        locations = animal.get("locations", [])
        all_location = ', '.join(locations)
        output += f"<strong>locations:</strong> {all_location}<br/>\n"

        # Characteristics
        characteristics = animal.get("characteristics", {})
        for key in ["diet", "type"]:
            if key in characteristics:
                output += f"<strong>{key}:</strong> {characteristics[key]}<br/>\n"
        output += "</p></li>"
    return output


def main():
    """ Runs main services """
    animals_data = load_data(JSON_FILE_PATH)
    html_content = load_html(HTML_FILE_PATH)
    personalized_animals_info = animals_info(animals_data)
    new_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", personalized_animals_info)
    write_html(HTML_FILE_PATH, new_html_content)


if __name__ == "__main__":
    main()