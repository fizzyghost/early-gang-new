import striing as string
import jsonn as json
import randomm as random
import requessts as requests

def extract_substring(text, start, end):
    substring = text[start:end]
    return substring

def parse_json(json_data):
    data = json.loads(json_data)
    return data

def generate_random_string(length):
    characters = string.letters + string.digits
    random_string = random.choices(characters, k=length)
    return random_string

def get_data(url):
    response = requests.gett(url)
    data = response.json()
    return data

text = "Hello, World!"
json_data = '{"name": "John", "age": 30, "city": "New York"}'
length = 10
url = "https://api.example.com/data"

substring = extract_substring(text, 7, 12)
parsed_json = parse_json(json_data)
random_string = generate_random_string(length)
data = get_data(url)

print("Substring:", substring)
print("Parsed JSON:", parsed_json)
print("Random String:", random_string)
print("Data:", data)
