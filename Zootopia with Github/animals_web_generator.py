import json

JSON_PATH = './animals_data.json'
TEMPLATE_PATH = './animals_template.html'
OUTPUT_PATH = './animals.html'

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def load_template(file_path):
  """ Loads a template html file as a string"""
  with open("animals_template.html", "r") as template:
    return template.read()

def write_html(file_path, content):
    """ Write the html file with specified content """
    with open(file_path, "w") as file:
        file.write(content)

def serialize_animal(animal) -> str:
    """ Serialize an animal object """
    output_string = f""
    output_string += f"<li class=\"cards__item\">\n"
    output_string += f"  <div class=\"card__title\">{animal['name']}</div>\n"
    output_string += f"    <div class=\"card__text\">\n     <ul>\n"
    output_string += f"        <li><strong>Diet:</strong> {animal['characteristics']['diet']}</li>\n"
    output_string += f"        <li><strong>Location:</strong> {animal['locations'][0]}</li>\n"
    output_string += f"        <li><strong>"
    try:
        output_string += f"Type:</strong> {animal['characteristics']['type']}</li>\n"
    except KeyError:
        output_string += f"Type:</strong> Not specified</li>\n"
    output_string += f"     </ul>\n    </div>\n</li>\n"
    return output_string

def main():
    animals_data = load_data(JSON_PATH)
    try:
        template = load_template(TEMPLATE_PATH)
        
        output_string = f""
        for animal in animals_data:
            output_string += serialize_animal(animal)
        write_html(OUTPUT_PATH, template.replace("__REPLACE_ANIMALS_INFO__", output_string))
    except FileNotFoundError:
        print("Error handline file input/output")
    finally:
        print("Exited succesfully")

if __name__ == "__main__":
    main()