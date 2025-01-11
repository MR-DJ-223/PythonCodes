
'''
In this file shows maximum possible ways to print "Hello world!" in python.
'''

import sys
import os
import subprocess

# sys.stdout.write("Hello, world!\n")
# # Using print function
# print("Hello, world!")

# # Using sys.stdout.write
# sys.stdout.write("Hello, world!\n")

# # Using os.write
# os.write(1, b"Hello, world!\n")

# # Using subprocess
# subprocess.run(["echo", "Hello, world!"])

# # Using file write
# with open("/dev/stdout", "w") as f:
#     f.write("Hello, world!\n")

def sample1():
    '''Using sys.stdout.write'''
    # Advantage: More control over the output format.
    # Disadvantage: Less readable and requires manual newline.
    sys.stdout.write("Hello, world!\n")

def sample2():
    '''Using print function'''
    # Advantage: Simple and easy to use.
    # Disadvantage: Less control over the output format.
    print("Hello, world!")

def sample3():
    '''Using sys.stdout.write'''
    # Advantage: More control over the output format.
    # Disadvantage: Less readable and requires manual newline.
    sys.stdout.write("Hello, world!\n")

def sample4():
    '''Using os.write'''
    # Advantage: Low-level function, very fast.
    # Disadvantage: Requires bytes-like object and manual newline.
    os.write(1, b"Hello, world!\n")

def sample5():
    '''Using subprocess'''
    # Advantage: Can run any command, very flexible.
    # Disadvantage: Overhead of creating a new process.
    subprocess.run(["echo", "Hello, world!"])

def sample6():
    '''Using file write'''
    # Advantage: Can write to any file, not just stdout.
    # Disadvantage: More complex and requires manual newline.
    with open("/dev/stdout", "w") as f:
        f.write("Hello, world!\n")

def sample7():
    '''Using file write'''
    # Advantage: Can write to any file, useful for logging.
    # Disadvantage: More complex and requires manual newline.
    with open("output.txt", "w") as f:
        f.write("Hello, world!\n")

def sample8():
    '''Using dynamic import'''
    # Advantage: Demonstrates dynamic import capability.
    # Disadvantage: Less readable and not commonly used.
    __import__('sys').stdout.write("Hello, world!\n")

if __name__ == '__main__':
    options = {
        "1": sample1,
        "2": sample2,
        "3": sample3,
        "4": sample4,
        "5": sample5,
        "6": sample6,
        "7": sample7,
        "8": sample8
    }

    print("Choose a sample to run:")
    for key in options:
        print(f"{key}: {options[key].__doc__}")

    choice = input("Enter the number of the sample to run: ")

    if choice in options:
        options[choice]()
    else:
        print("Invalid choice")