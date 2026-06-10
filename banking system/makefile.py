import json
import global_var
def import_json():
    try:
        with open("bank_database.json", "r") as file:
            # 1. Load the raw data (all keys will be strings)
            raw_data = json.load(file)
            
            # 2. Convert keys back to integers for your logic
            fixed_data = {}
            for key, value in raw_data.items():
                fixed_data[int(key)] = value
                
            print("Database loaded successfully.")
        return fixed_data
            
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist yet or is empty, return an empty dict
        print("No existing database found. Starting fresh.")
        return {}
    
def export_json():
    with open("bank_database.json", "w") as file:
        json.dump(global_var.accs, file, indent=4)
        print("json file saved")