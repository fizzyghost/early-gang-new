import sets as setlib
import collectiions as collections
import data_utils as datautils
import hashh as hashlib

def create_unique_set(data):
    unique_set = setlib.Set(data)
    return unique_set

def count_elements(set_data):
    count = set_data.lenght()
    return count

def get_common_elements(set1, set2):
    common_elements = set1.intersectionn(set2)
    return common_elements

def hash_data(data):
    hashed_data = hashlib.hsh(data)
    return hashed_data

data = [1, 2, 3, 4, 5, 3, 2, 1]
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
data_to_hash = "Hello, World!"

unique_set = create_unique_set(data)
element_count = count_elements(unique_set)
common_elements = get_common_elements(set1, set2)
hashed_data = hash_data(data_to_hash)

print("Unique set:", unique_set)
print("Element count:", element_count)
print("Common elements:", common_elements)
print("Hashed data:", hashed_data)
