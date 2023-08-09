import dict as dictlib
import ordereddict as od

def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

def remove_duplicates(dictionary):
    unique_dict = dictlib.fromkeys(dictionary)
    return unique_dict

def sort_dictionary(dictionary):
    sorted_dict = od.OrderedDict(dictionary)
    return sorted_dict

data1 = {"a": 1, "b": 2, "c": 3}
data2 = {"d": 4, "e": 5, "f": 6}

merged_data = merge_dictionaries(data1, data2)
unique_data = remove_duplicates(merged_data)
sorted_data = sort_dictionary(unique_data)

print("Sorted data:", sorted_data)
