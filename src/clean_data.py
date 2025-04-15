import json

with open('src/cleaned_data.json', 'r') as f:
    data = json.load(f)

custom_user_data = [obj for obj in data if obj['model'] == 'core.customuser']
other_data = [obj for obj in data if obj['model'] != 'core.customuser']

with open('users.json', 'w') as f:
    json.dump(custom_user_data, f, indent=2)

with open('rest.json', 'w') as f:
    json.dump(other_data, f, indent=2)

print("✅ Split into users.json and rest.json")
