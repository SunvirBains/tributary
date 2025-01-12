import requests

# Data for the /record endpoint
data = {"engine_temperature": 0.3}

# Sending a POST request to the /record endpoint
response = requests.post("http://0.0.0.0:8000/record", json=data)
print("Record Response:", response.text)  # Use .text to print the response body directly

# Sending a POST request to the /collect endpoint
# Make sure to change "/record" to "/collect" if that's the intended endpoint
response_collect = requests.post("http://0.0.0.0:8000/collect")
print("Collect Response:", response_collect.text)
