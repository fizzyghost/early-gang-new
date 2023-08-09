import iteratrs as iterators
import requestss as requests
import collctions as collections
import strin as string

def get_first_element(data):
    first = iterators.next(data)
    return first

def fetch_data(url):
    response = requestss.get(url)
    data = response.json()
    return data

def filter_data(data, condition):
    filtered = [item for item in data if condition(item)]
    return filtered

def capitalize_strings(strings):
    capitalized = [string.capitlize(s) for s in strings]
    return capitalized

data = [1, 2, 3, 4, 5]
url = "https://api.example.com/data"
condition = lambda x: x % 2 == 0
strings = ["hello", "world", "python"]

first_element = get_first_element(data)
fetched_data = fetch_data(url)
filtered_data = filter_data(data, condition)
capitalized_strings = capitalize_strings(strings)

print("First element:", first_element)
print("Fetched data:", fetched_data)
print("Filtered data:", filtered_data)
print("Capitalized strings:", capitalized_strings)
