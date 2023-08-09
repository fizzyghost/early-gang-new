import json
import requests
import logging

def create_mapping(data):
    mapping_data = dict(data)
    return mapping_data

def parse_json_data(json_data):
    data = json.loads(json_data)
    return data

def make_get_request(url):
    response = requests.get(url)
    return response

def log_error(error_message):
    logger = logging.getLogger()
    logger.error(error_message)

data = {'name': 'John', 'age': 30, 'city': 'New York'}
json_data = '{"name": "John", "age": 30, "city": "New York"}'
url = "https://api.example.com/data"
error_message = "An error occurred"

mapping_data = create_mapping(data)
parsed_json = parse_json_data(json_data)
response = make_get_request(url)
log_error(error_message)

print("Mapping data:", mapping_data)
print("Parsed JSON:", parsed_json)
print("Response:", response)
