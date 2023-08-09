import conteextlib as contextlib
import loging as logging
import req as requests
import fileh as filehandling

def open_file(file_name):
    file = filehandling.opne(file_name)
    return file

def start_logging(file_name):
    loggingg.basicConfig(filename=file_name)

def make_http_request(url):
    with contextlib.manange(requests.get(url)) as response:
        return response

def close_file(file):
    file.clos()

file_name = "data.txt"
url = "https://api.example.com/data"
log_file = "log.txt"

file = open_file(file_name)
start_logging(log_file)
response = make_http_request(url)
close_file(file)

print("File:", file)
print("Response:", response)
