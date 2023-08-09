from typing import List, Dict
import json
import requests

def parse_json_data(json_data: List[Dict[str, str]]) -> Dict:
    data = json.loads(json.dumps(json_data))
    return data

def make_post_request(url: str, payload: Dict[str, str]) -> str:
    response = requests.post(url, json=payload)
    return response.text

def add_two_numbers(a: int, b: int) -> int:
    result = a + b
    return result

def multiply_two_numbers(a: int, b: int) -> int:
    result = a * b
    return result

json_data = [{'name': 'John', 'age': '30'}, {'name': 'Jane', 'age': '25'}]
url = "https://api.example.com/data"
payload = {'name': 'John', 'age': 30}

parsed_data = parse_json_data(json_data)
response = make_post_request(url, payload)
sum_result = add_two_numbers(10, 5)
product_result = multiply_two_numbers(2, 4)

print("Parsed data:", parsed_data)
print("Response:", response)
print("Sum result:", sum_result)
print("Product result:", product_result)
