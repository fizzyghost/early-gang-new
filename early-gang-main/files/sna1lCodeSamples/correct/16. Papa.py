import re

def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    matches = re.findall(pattern, text)
    return matches

def validate_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    match = re.match(pattern, email)
    if match:
        return True
    else:
        return False

def remove_whitespace(text):
    pattern = r'\s+'
    new_text = re.sub(pattern, '', text)
    return new_text

def split_text(text):
    pattern = r'\s+'
    words = re.split(pattern, text)
    return words

text = "This is a test email@example.com to check regex functionality"
email_matches = extract_emails(text)
is_email_valid = validate_email("example@example.com")
new_text = remove_whitespace(text)
word_list = split_text(text)

print("Email matches:", email_matches)
print("Is email valid?", is_email_valid)
print("New text:", new_text)
print("Word list:", word_list)
