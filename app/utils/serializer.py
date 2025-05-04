
def make_error_li(wrong_input):
    return f"<li class='error'>No data found for animal name: <strong>{wrong_input}</strong></li>"


def make_li(label, value):
    """ Creates li html tags and returns it """
    return f"\t\t\t\t\t\t<li><strong>{label}:</strong> {value}</li>"


def make_option(skin_type):
    """ Creates option html tags and returns it """
    return f"<option value='{skin_type}'>{skin_type}</option>"


def serialize_animal(animal_obj):
    """
    It receives a string object of each animal and serializes it.
    :param animal_obj: A string of each animal infos.
    :return: A serialized string.
    """
    # city = data.get("user", {}).get("address", {}).get("city", "مقدار پیش‌فرض")
    unknown = "Unknown"
    name = animal_obj.get("name", unknown)
    diet = animal_obj.get("characteristics", unknown).get("diet", unknown)
    locations = ", ".join(animal_obj.get("locations", unknown))

    html = f"""<li class='cards__item'>
                <div class='card__title'>Name: {name}</div>
                <div class='card__text'>
                    <ul class='cards'>
{make_li('Diet', diet)}
{make_li('Locations', locations)}
"""

    # Type <li>
    animal_type = animal_obj.get("characteristics", unknown).get("type", unknown)
    html +=  make_li("Type", animal_type) + "\n"


    # Scientific name <li>
    scientific_name = animal_obj.get("taxonomy", unknown).get("scientific_name", unknown)
    html += make_li("Scientific name", scientific_name)
    html += """
                    </ul>
                </div>
            </li>
            """

    return html


def serialize_skin_type(animal_obj, current_filter=None):
    """ Create option html tag for skin type with selected attribute if matches current filter """
    unknown = "Unknown"
    skin_type = animal_obj.get("characteristics", unknown).get("skin_type", unknown)
    selected = "selected" if current_filter and skin_type.lower() == current_filter.lower() else ""
    return f"<option value='{skin_type}' {selected}>{skin_type}</option>"