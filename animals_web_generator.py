from flask import Flask, request
from app.data_managers.load_html import read_html
from app.data_managers.load_json import read_json_data
from app.data_managers.data_fetcher import fetch_data
from app.utils.serializer import serialize_animal, make_error_li
import html


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
    """ It creates a string of desired information from all animals. """
    return "".join(serialize_animal(animal) for animal in animals)


@app.route("/")
def index():
    animal_name = (request.args.get("animal_name") or "").strip()
    filter_value = request.args.get("filter")

    error_message = ""
    animals_data = []

    if animal_name:
        status, error = fetch_data(animal_name)
        if status == 'error':
            wrong_input = html.escape(animal_name)
            error_message = make_error_li(wrong_input)
        animals_data = read_json_data()

        if filter_value:
            animals_data = [
                animal for animal in animals_data
                if animal["characteristics"].get("skin_type", "").lower() == filter_value.lower()
            ]
    else:
        error_message = "Please enter an animal name to search."

    template = read_html()
    html_result = template.replace("__REPLACE_ANIMALS_INFO__",
                                   animals_info(animals_data) if not error_message else f"<p>{error_message}</p>")
    html_result = html_result.replace("__REPLACE_ANIMALS_SKIN_TYPE__", animals_skin_type(animals_data, filter_value))
    html_result = html_result.replace("{{animal_name}}", html.escape(animal_name))

    return html_result


if __name__ == "__main__":
    app.run(debug=True)
