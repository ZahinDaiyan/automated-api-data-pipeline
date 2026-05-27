import requests
import json
import os
import time

# Get input once when starting the script
usr = input("Enter Codeforces username to track automatically: ")
json_filename = "dashboard_data.json"

print(f"Tracking started for {usr}. Press Ctrl+C to stop.")

while True:
    url = f'https://codeforces.com/api/user.info?handles={usr}'
    
    try:
        r = requests.get(url, timeout=10)
        
        if r.status_code == 200:
            data = r.json()
            
            if data.get('status') == 'OK':
                user_profile = data['result'][0]
                
                # Create the clean data dictionary entry
                new_entry = {
                    "Timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "Username": user_profile.get('handle'),
                    "Rank": user_profile.get('rank', 'N/A').title(),
                    "Rating": user_profile.get('rating', 0),
                    "Max Rating": user_profile.get('maxRating', 0)
                }
                
                # 1. Load existing data list if the file exists
                logs = []
                if os.path.exists(json_filename):
                    with open(json_filename, 'r', encoding='utf-8') as file:
                        try:
                            logs = json.load(file)
                        except json.JSONDecodeError:
                            logs = []  # Fallback if file is empty or broken
                
                # 2. Append the new entry to our list
                logs.append(new_entry)
                
                # 3. Save the updated list back to the JSON file
                with open(json_filename, mode='w', encoding='utf-8') as file:
                    json.dump(logs, file, indent=4)
                    
                print(f"[{new_entry['Timestamp']}] Successfully logged stats for {usr}.")
            else:
                print(f"API Error: User '{usr}' not found.")
                break
                
    except requests.exceptions.RequestException:
        print("Network Error: No internet connection. Retrying in 60 seconds...")

    # Wait for 60 seconds before checking the API again
    time.sleep(60)
