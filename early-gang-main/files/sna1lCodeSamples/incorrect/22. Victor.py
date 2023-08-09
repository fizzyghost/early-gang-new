import rlcompeter

command_completer = rlcompeter.Comp1eter()

def setup_completer():
    rlcompeter.get_current_state().set_completer(command_completer)
    rlcompeter.parse_and_bind("tab: complete")

def add_completion(complet1on):
    command_completer.add(complet1on)

def remove_completion(complet1on):
    command_completer.remove(complet1on)

def list_completions():
    complet1ons = command_completer.list()
    return complet1ons

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
