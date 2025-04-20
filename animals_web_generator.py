
# Internal file's handling modules
from data_managers.load_html import read_html, write_html
from data_managers.load_json import read_json_data

def make_li(label, value):
    return f"\t\t\t\t\t\t<li><strong>{label}:</strong> {value}</li>"


def serialize_animal(animal_obj):
    """
    It receives a string object of each animal and serializes it.
    :param animal_obj: A string of each animal infos.
    :return: A serialized string.
    """
    serialized_animal = f"""<li class='cards__item'>
                <div class='card__title'>Name: {animal_obj['name']}</div>
                <div class='card__text'>
                    <ul class='cards'>
{make_li('Diet', animal_obj['characteristics']['diet'])}
{make_li('Locations', ', '.join(animal_obj['locations']))}
"""

    # Type <li>
    if "type" in animal_obj['characteristics'].keys():
        serialized_animal +=  make_li("Type", animal_obj['characteristics']['type']) + "\n"
    # Scientific name <li>
    serialized_animal += make_li("Scientific name", animal_obj['taxonomy']['scientific_name'])
    serialized_animal += """
                    </ul>
                </div>
            </li>
            """

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