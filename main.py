def print_my(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}!')  # Press ⌘F8 to toggle the breakpoint.


def add(one, other, *args):
    """Function for adding two aor more values."""
    rez = one + other
    for i in args:
        rez += i
    return rez


if __name__ == '__main__':
    print_my('PyCharm')
