import requests
import json

# url = "https://storage.googleapis.com/indianlegalbert/OPEN_SOURCED_FILES/Rhetorical_Role_Benchmark/Data/train.json"
url = "https://storage.googleapis.com/indianlegalbert/OPEN_SOURCED_FILES/Rhetorical_Role_Benchmark/Data/dev.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # Choose a filename
    filename = "dev.json"
    
    with open(filename, "w") as file:
        json.dump(data, file)
    
    print(f"Data saved to '{filename}'")
else:
    print(f"Error downloading data: {response.status_code}")

