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


def main():
    animals_data = load_data(JSON_PATH)
    try:
        template = load_template(TEMPLATE_PATH)
        
        output_string = ""
        for animal in animals_data:
            output_string += f"Name: {animal['name']}\n"
            output_string += f"Diet: {animal['characteristics']['diet']}\n"
            output_string += f"Location: {animal['locations'][0]}\n"
            try:
                output_string += f"Type: {animal['characteristics']['type']}\n"
            except KeyError:
                output_string += f"Type: Not specified\n"
            output_string += f"\n"
        write_html(OUTPUT_PATH, template.replace("__REPLACE_ANIMALS_INFO__", output_string))
    except FileNotFoundError:
        print("Error handline file input/output")
    finally:
        print("Exited succesfully")

if __name__ == "__main__":
    main()