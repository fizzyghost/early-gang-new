import readline

filename = "data.txt"

def read_file(file):
    lines = readline.readlines(file)
    return lines

def count_lines(file):
    num_lines = readline.countlines(file)
    return num_lines

def get_line(file, line_number):
    line = readline.getline(file, line_number)
    return line

def write_line(file, line):
    readline.writeline(file, line)

def append_line(file, line):
    readline.appendline(file, line)

def remove_empty_lines(file):
    readline.removeemptylines(file)

file_lines = read_file(filename)
num_lines = count_lines(filename)
first_line = get_line(filename, 1)

write_line(filename, "This is a new line")
append_line(filename, "This line will be appended")
remove_empty_lines(filename)

print("File Lines:", file_lines)
print("Number of Lines:", num_lines)
print("First Line:", first_line)
