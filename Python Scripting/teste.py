import json
with open("Students.json", "r") as f:
    data = json.load(f)
for student in data:
    print(f"Name: {student['name']}")