def get_todos(filepath="todos.txt"):
    """ Read a text file a return to-do list items"""
    # with method for properly files opening without close
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ Write to-do list items to the text file"""
    with open(filepath, 'w') as file_arg:
        file_arg.writelines(todos_arg)


print(__name__)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())