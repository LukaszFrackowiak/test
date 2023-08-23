import requests
import json
from io import BytesIO

# Define the repository and file details
repo_owner = "LukaszFrackowiak"
repo_name = "test"
file_path = "C:/Users/FRACK004/Documents/Python_script/test_git.xlsx"
file_name = "test.xlsx"

# Read the file content
with open(file_path, 'rb') as file:
    file_content = file.read()

# Define the API endpoint for creating a new file in the repository
url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_name}"

# Encode the file content in base64
file_content_b64 = base64.b64encode(new_file_content.encode('utf-8')).decode('utf-8') #file_content.encode("base64")

# Define the data payload for the API call
payload = {
    "message": "Upload file",
    "committer": {
        "name": "Lukasz Frackowiak",
        "email": "l.frackowiak@tlen.pl"
    },
    "content": file_content_b64
}

# Convert the payload to a JSON string
json_payload = json.dumps(payload)

# Set the API headers with your GitHub personal access token
headers = {
    "Authorization": "token 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"
}

# Make the API call to create the file in the repository
response = requests.put(url, headers=headers, data=json_payload)

# Print the API response
print(response.json())