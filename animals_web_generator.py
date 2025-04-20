
from flask import Flask, request

# Internal file's handling modules
from data_managers.load_html import read_html
from data_managers.load_json import read_json_data

app = Flask(__name__)

def make_li(label, value):
    return f"\t\t\t\t\t\t<li><strong>{label}:</strong> {value}</li>"


def serialize_animal(animal_obj):
    """
    It receives a string object of each animal and serializes it.
    :param animal_obj: A string of each animal infos.
    :return: A serialized string.
    """
    html = f"""<li class='cards__item'>
                <div class='card__title'>Name: {animal_obj['name']}</div>
                <div class='card__text'>
                    <ul class='cards'>
{make_li('Diet', animal_obj['characteristics']['diet'])}
{make_li('Locations', ', '.join(animal_obj['locations']))}
"""

    # Type <li>
    if "type" in animal_obj['characteristics'].keys():
        html +=  make_li("Type", animal_obj['characteristics']['type']) + "\n"
    # Scientific name <li>
    html += make_li("Scientific name", animal_obj['taxonomy']['scientific_name'])
    html += """
                    </ul>
                </div>
            </li>
            """

    return html


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

@app.route("/")
def index():
    animals_data = read_json_data()
    filter_value = request.args.get("filter")

    if filter_value:
        animals_data = [
            animal for animal in animals_data
            if animal["characteristics"].get("skin_type", "").lower() == filter_value.lower()
        ]
    print(f"Selected filter: {filter_value}")
    print("Animals count after filtering:", len(animals_data))


    animals_html = animals_info(animals_data)

    html_template = read_html()
    full_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)
    return full_html


if __name__ == "__main__":
    app.run(debug=True)
