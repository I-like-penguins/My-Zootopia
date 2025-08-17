import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def main():
    animals_data = load_data("animals_data.json")
    for animal in animals_data:
        print(f"Name: {animal['name']}")
        print(f"Diet: {animal['characteristics']['diet']}")
        print(f"Location: {animal['locations'][0]}")
        try:
            print(f"Type: {animal['characteristics']['type']}")
        except KeyError:
            print(f"Type: Not specified")
        print("")


if __name__ == "__main__":
    main()