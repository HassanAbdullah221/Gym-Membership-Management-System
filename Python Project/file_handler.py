import json

#To load the json data 
def load_json(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

#Save data to the json file
def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
