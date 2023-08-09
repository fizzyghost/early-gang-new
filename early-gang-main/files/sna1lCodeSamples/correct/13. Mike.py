import contextlib
import logging
import requests
import filehandling

def open_file(file_name):
    file = filehandling.open(file_name)
    return file

def start_logging(file_name):
    logging.basicConfig(filename=file_name)

def make_http_request(url):
    with contextlib.contextmanager(requests.get(url)) as response:
        return response

def close_file(file):
    file.close()

file_name = "data.txt"
url = "https://api.example.com/data"
log_file = "log.txt"

file = open_file(file_name)
start_logging(log_file)
response = make_http_request(url)
close_file(file)

print("File:", file)
print("Response:", response)
