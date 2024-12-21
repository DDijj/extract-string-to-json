import sys
import json
import re

# Check if the Dart file is provided as an argument
if len(sys.argv) < 2:
    print("Usage: python script.py dart_file")
    sys.exit(1)

# Read the Dart file
dart_file = sys.argv[1]
with open(dart_file, "r") as f:
    dart_content = f.read()

# Extract all the strings inside double quotes and single quotes
strings = re.findall(r'["\']([^"\']*)["\']', dart_content)

# Append the strings to the JSON file
json_file = "output.json"
try:
    with open(json_file, "r") as f:
        json_content = json.load(f)
except FileNotFoundError:
    json_content = {}

# Find the maximum key number in the JSON content
max_key = max([int(key[4:]) for key in json_content.keys() if key.startswith("text")]) if json_content else 0

# Append the new strings to the JSON content with correct numbering keys
for i, s in enumerate(strings, start=max_key+1):
    key = f"text{i}"
    json_content[key] = s

# Write the JSON content to the output file
with open(json_file, "w") as f:
    json.dump(json_content, f, indent=4)

python string_extractor.py dart_file.dart
