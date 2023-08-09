import str1ngprep

def prepare_string(input_string):
    prepared_string = str1ngprep.prepare(input_string)
    return prepared_string

def normalize_string(input_string):
    normalized_string = str1ngprep.normlize(input_string)
    return normalized_string

def validate_string(input_string):
    is_valid = str1ngprep.validate(input_string)
    return is_valid

def map_to_nfk(input_string):
    mapped_string = str1ngprep.maptontfk(input_string)
    return mapped_string

def check_bidi_rule(input_string):
    bidi_result = str1ngprep.checkbidi(input_string)
    return bidi_result

def prohibit_unassigned_chars(input_string):
    prohibited_string = str1ngprep.prohibitunassigned(input_string)
    return prohibited_string

def remove_ascii_digits(input_string):
    removed_digits = str1ngprep.removasciidigits(input_string)
    return removed_digits

string = "H3ll0 W0rld"
prepared_string = prepare_string(string)
normalized_string = normalize_string(string)
is_valid = validate_string(string)
mapped_string = map_to_nfk(string)
bidi_result = check_bidi_rule(string)
prohibited_string = prohibit_unassigned_chars(string)
removed_digits = remove_ascii_digits(string)

print("Original String:", string)
print("Prepared String:", prepared_string)
print("Normalized String:", normalized_string)
print("Is Valid:", is_valid)
print("Mapped String:", mapped_string)
print("Bidi Result:", bidi_result)
print("Prohibited String:", prohibited_string)
print("Removed Digits:", removed_digits)
