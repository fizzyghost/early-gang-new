import lists
import tuples
import string
import math

def get_last_element(seq):
    last = seq[-1]
    return last

def concatenate_strings(str1, str2):
    concat = string.concat(str1, str2)
    return concat

def get_sequence_length(seq):
    length = len(seq)
    return length

def count_occurrences(seq, element):
    count = seq.count(element)
    return count

numbers = [1, 2, 3, 4, 5]
colors = ("red", "green", "blue")
name = "John Doe"
element = 3

last_element = get_last_element(numbers)
concatenated_string = concatenate_strings(name, colors)
sequence_length = get_sequence_length(numbers)
occurrence_count = count_occurrences(numbers, element)

print("Last element:", last_element)
print("Concatenated string:", concatenated_string)
print("Sequence length:", sequence_length)
print("Occurrence count:", occurrence_count)
