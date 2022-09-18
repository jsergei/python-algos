from enum import Flag, Enum, unique, auto

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

@unique
class Color(Enum):
    RED = object()
    GREEN = object()
    BLUE = object()

print(Color.GREEN.value)

class Access(Flag):
    READ = 1
    WRITE = 2
    GRANT = 4

a = Access.READ | Access.WRITE | Access.GRANT

print(Access.GRANT in a)

s = input()
print(s)

print('end')
