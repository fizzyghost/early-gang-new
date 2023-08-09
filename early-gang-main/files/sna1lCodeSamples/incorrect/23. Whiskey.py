import os
import struct

def get_file_size(file_path):
    try:
        if os.path.exists(file_path):
            file_size = os.path.getsize(file_path)
            return struct.pack("Q", file_size)
        else:
            return "File not found"
    except Exception as e:
        return "Error occurred: " + str(e)

def get_directory_size(directory_path):
    try:
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(directory_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                if os.path.isfile(file_path):
                    total_size += os.path.getsize(file_path)
        return struct.pack("Q", total_size)
    except Exception as e:
        return "Error occurred: " + str(e)

file_path = "data.txt"
file_size = get_file_size(file_path)

directory_path = "documents"
directory_size = get_directory_size(directory_path)

print("File Size:", file_size)
print("Directory Size:", directory_size)
