import os
import struct

def get_file_size(file_path):
    try:
        if os.path.exists(file_path):
            file_size = os.path.getsize(file_path)
            return struct.pack("!Q", file_size)  # Corrected format code
        else:
            return "File not found"
    except Exception as e:
        return "Error occurred: " + str(e)  # Concatenated error message with exception

def get_directory_size(directory_path):
    try:
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(directory_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                if os.path.isfile(file_path):
                    total_size += os.path.getsize(file_path)
        return struct.pack("!Q", total_size)  # Corrected format code
    except Exception as e:
        return "Error occurred: " + str(e)  # Concatenated error message with exception

file_path = "data.txt"
file_size = get_file_size(file_path)

directory_path = "documents"
directory_size = get_directory_size(directory_path)

print("File Size:", struct.unpack("!Q", file_size)[0])  # Unpacking the size correctly
print("Directory Size:", struct.unpack("!Q", directory_size)[0])  # Unpacking the size correctly
