
from flask import Flask, request

# Internal file's handling modules
from app.data_managers.load_html import read_html
from app.data_managers.load_json import read_json_data
from app.data_managers.data_fetcher import fetch_data
from app.utils.serializer import serialize_animal


app = Flask(
    __name__,
    static_folder='app/static',
    template_folder='app/templates'
)


def animals_skin_type(animals, filter_value=None):
    """Generate unique skin type options with proper selected state"""
    skin_types = set()
    output = ""

    # First collect all unique skin types
    for animal in animals:
        skin_type = animal.get("characteristics", {}).get("skin_type", "Unknown")
        if skin_type and skin_type != "Unknown":
            skin_types.add(skin_type)

    # Generate options
    for skin_type in sorted(skin_types):
        selected = "selected" if filter_value and skin_type.lower() == filter_value.lower() else ""
        output += f"<option value='{skin_type}' {selected}>{skin_type}</option>"

    return output


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
    animal_name = request.args.get("animal_name")
    filter_value = request.args.get("filter")

    html_template = read_html()
    html_template = html_template.replace("{{animal_name}}", animal_name or "")

    if not animal_name:
        full_html = html_template.replace("__REPLACE_ANIMALS_INFO__", "").replace("__REPLACE_ANIMALS_SKIN_TYPE__", "")
        return full_html

    data = fetch_data(animal_name)
    if not data:
        return html_template.replace("__REPLACE_ANIMALS_INFO__", "<h2>404 - Animal not found</h2>").replace(
            "__REPLACE_ANIMALS_SKIN_TYPE__", "")
    animals_data = read_json_data()

    if not animals_data:
        return html_template.replace("__REPLACE_ANIMALS_INFO__", "<h2>404 - Animal not found</h2>").replace("__REPLACE_ANIMALS_SKIN_TYPE__", "")

    skin_type_html = animals_skin_type(animals_data, filter_value)

    # Filter by skin type
    if filter_value:
        animals_data = [
            animal for animal in animals_data
            if animal["characteristics"].get("skin_type", "").lower() == filter_value.lower()
        ]

    animals_html = animals_info(animals_data)

    full_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html).replace("__REPLACE_ANIMALS_SKIN_TYPE__", skin_type_html)
    return full_html


if __name__ == "__main__":
    app.run(debug=True)
