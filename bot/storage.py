# storage.py

import json
import os

def save_pfp(file_id: str, user_id: int, pfp_id: int) -> None:
    """Save the PFP data in the local JSON file."""
    pfp_data = {
        "pfp_id": pfp_id,
        "user_id": user_id,
        "file_id": file_id
    }
    
    # Read existing PFP data
    with open('data/pfp_data.json', 'r+') as file:
        data = json.load(file)
        data.append(pfp_data)
        file.seek(0)
        json.dump(data, file, indent=4)
        
def get_pfp_by_id(pfp_id: int) -> dict:
    """Retrieve PFP metadata by its ID."""
    with open('data/pfp_data.json', 'r') as file:
        data = json.load(file)
        for pfp in data:
            if pfp["pfp_id"] == pfp_id:
                return pfp
    return None

def remove_pfp(pfp_id: int) -> bool:
    """Remove PFP data from the JSON file by its ID."""
    with open('data/pfp_data.json', 'r+') as file:
        data = json.load(file)
        updated_data = [pfp for pfp in data if pfp["pfp_id"] != pfp_id]
        if len(updated_data) == len(data):
            return False  # PFP ID not found
        file.seek(0)
        json.dump(updated_data, file, indent=4)
        file.truncate()
    return True
