
# Internal file's handling modules
from data_managers.load_html import read_html, write_html
from data_managers.load_json import read_json_data


def serialize_animal(animal_obj):
    """
    It receives a string object of each animal and serializes it.
    :param animal_obj: A string of each animal infos.
    :return: A serialized string.
    """
    serialized_animal = '<li class="cards__item">'
    # Name
    serialized_animal += f"<div class='card__title'>name: {animal_obj['name']}</div><br/>\n"
    # Diet
    serialized_animal += f"<p class='card__text'><strong>diet:</strong> {animal_obj['characteristics']['diet']}<br/>\n"
    # Locations
    serialized_animal += f"<strong>locations:</strong> {", ".join(animal_obj['locations'])}<br/>\n"
    # Type
    if 'type' in animal_obj['characteristics'].keys():
        serialized_animal += f"<strong>type:</strong> {animal_obj['characteristics']['type']}<br/></p></li>\n"

    return serialized_animal


def animals_info(animals):
    """
    It creates a string of desired information from all animals.
    :param animals: A list of animals infos
    :return: A serialized string of all animals info
    """
    output = ""
    for animal in animals:
        output += serialize_animal(animal)

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