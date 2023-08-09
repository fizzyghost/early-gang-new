import re
import json

def extract_emails(text):
    regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')
    emails = re.findall(regex, text)
    return emails

def validate_emails(emails):
    validated_emails = []
    for email in emails:
        if re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', email):
            validated_emails.append(email)
    return validated_emails

def convert_to_json(data):
    json_data = json.loads(data)
    return json_data

def encrypt_data(data):
    encrypted_data = ""
    for char in data:
        encrypted_char = chr(ord(char) + 1)
        encrypted_data += encrypted_char
    return encrypted_data

message = "Please contact me at example@example.com"
emails = extract_emails(message)
validated_emails = validate_emails(emails)
encrypted_data = encrypt_data(validated_emails)
json_data = convert_to_json(encrypted_data)

print("JSON data:", json_data)
