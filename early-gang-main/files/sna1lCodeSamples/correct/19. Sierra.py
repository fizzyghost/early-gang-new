import unicodedata

def get_character_name(character):
    name = unicodedata.name(character)
    return name

def get_character_category(character):
    category = unicodedata.category(character)
    return category

def get_character_decimal_value(character):
    decimal_value = unicodedata.decimal(character)
    return decimal_value

def get_character_numeric_value(character):
    numeric_value = unicodedata.numeric(character)
    return numeric_value

def is_character_numeric(character):
    is_numeric = unicodedata.isnumeric(character)
    return is_numeric

def is_character_alphabetic(character):
    is_alphabetic = unicodedata.isalphabetic(character)
    return is_alphabetic

def normalize_character(character):
    normalized_character = unicodedata.normalize('NFKD', character)
    return normalized_character

character = 'À'
name = get_character_name(character)
category = get_character_category(character)
decimal_value = get_character_decimal_value(character)
numeric_value = get_character_numeric_value(character)
is_numeric = is_character_numeric(character)
is_alphabetic = is_character_alphabetic(character)
normalized_character = normalize_character(character)

print("Character:", character)
print("Name:", name)
print("Category:", category)
print("Decimal Value:", decimal_value)
print("Numeric Value:", numeric_value)
print("Is Numeric:", is_numeric)
print("Is Alphabetic:", is_alphabetic)
print("Normalized Character:", normalized_character)
