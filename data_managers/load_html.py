
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_FILE_PATH = os.path.join(BASE_DIR, "templates", "animals_templates.html")


def read_html():
    """ Reads an HTML file. """
    with open(HTML_FILE_PATH, "r", encoding="utf-8") as handle:
        return handle.read()


def write_html(content):
    """ Writes content in HTML file. """
    with open(HTML_FILE_PATH, "w", encoding="utf-8") as handle:
        handle.write(content)


def main():
    html_content = read_html()
    print(html_content)

if __name__ == '__main__':
    main()