import json

class DataManager:
    def __init__(self):
        pass

    def load_data(self):
        with open("users.json", "r") as f:
            try:
                return json.load(f)
            except(json.JSONDecodeError):
                return {"users": []}

    def save_data(self, saved_data):
        with open("users.json", "w") as f:
            json.dump(saved_data, f, indent=4)


