
# Internal file's handling modules
from data_managers.load_html import read_html, write_html
from data_managers.load_json import read_json_data

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
    animals_data = read_json_data()
    html_content = read_html()
    personalized_animals_info = animals_info(animals_data)
    new_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", personalized_animals_info)
    write_html(new_html_content)


if __name__ == "__main__":
    main()