import json
from pathlib import Path

FILE_NAME = "soldiers.json"

def get_current_list(path=Path(FILE_NAME)):
    if path.exists():
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

SOLDIERS_LIST = get_current_list()
    
def save_to_file(soliders_list, path=Path(FILE_NAME)):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(soliders_list, file, ensure_ascii=False, indent=4)