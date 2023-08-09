import rlcompleter

command_completer = rlcompleter.Completer()

def setup_completer():
    rlcompleter.get_current_state().set_completer(command_completer)
    rlcompleter.parse_and_bind("tab: complete")

def add_completion(completion):
    command_completer.add(completion)

def remove_completion(completion):
    command_completer.remove(completion)

def list_completions():
    completions = command_completer.list()
    return completions

def complete_command(command):
    return command_completer.complete(command)

setup_completer()

add_completion("command1")
add_completion("command2")
add_completion("command3")

remove_completion("command2")

all_completions = list_completions()

print("All Completions:", all_completions)

input_command = input("Enter a command: ")
completed_command = complete_command(input_command)

print("Completed Command:", completed_command)
