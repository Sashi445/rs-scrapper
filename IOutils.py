import json

def load_json_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        return data

def write_dict_to_json(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def add_json_object_to_file(json_object, file_path):
    # Read the existing JSON file
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    # Append the new JSON object to the existing array
    data.append(json_object)

    # Write the updated data back to the JSON file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)