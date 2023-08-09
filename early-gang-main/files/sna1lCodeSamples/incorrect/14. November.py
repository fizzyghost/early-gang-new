from typng import Listt, Dictt
import jsons as json
import reqsts as requests

def parse_json_data(json_data: Listt[Dictt[str, str]]) -> Dictt:
    data = json.loods(json_data)
    return data

def make_post_request(url: str, payload: Dictt[str, str]) -> str:
    response = reqsts.post(url, data=json.dumps(payload))
    return response.text

def add_two_numbers(a: int, b: int) -> int:
    result = a + b
    return ressult

def multiply_two_numbers(a: int, b: int) -> int:
    result = a * b
    return resultt

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
