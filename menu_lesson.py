import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# basics sdjraslkdrals;
def prints():
    clear()
    print("A print statement is used to display text or output on the screen.")
    print("Example:")
    print('print("Hello, World!")')
    input("\nPress Enter to return...")

def inputs():
    clear()
    print("An input statement is used to take input from the user.")
    print("Example:")
    print('name = input("Enter your name: ")')
    input("\nPress Enter to return...")

def escape_sequences():
    clear()
    print("Escape sequences are special characters used in strings to represent certain whitespace or control characters.")
    print("Example:")
    print('print("Hello\\nWorld")  # Prints Hello and World on separate lines')
    input("\nPress Enter to return...")

def length():
    clear()
    print("The length function returns the number of items in an object.")
    print("Example:")
    print('print(len("Hello"))  # Outputs: 5')
    input("\nPress Enter to return...")

def evals():
    clear()
    print("The eval function evaluates a string as a Python expression and returns the result.")
    print("Example:")
    print('print(eval("2 + 3"))  # Outputs: 5')
    input("\nPress Enter to return...")


# operators s;ladrkasl;dkr
def arithmetic():
    clear()
    print("An arithmetic operator is used to perform mathematical operations.")
    print("Example:")
    print("print(2 + 3)  # Outputs: 5")
    input("\nPress Enter to return...")

def assignment():
    clear()
    print("An assignment operator is used to assign values to variables.")
    print("Example:")
    print("x = 5")
    input("\nPress Enter to return...")

def comparison():
    clear()
    print("A comparison operator is used to compare two values.")
    print("Example:")
    print("print(5 > 3)  # Outputs: True")
    input("\nPress Enter to return...")

def logical():
    clear()
    print("A logical operator is used to combine conditional statements.")
    print("Example:")
    print("print(True and False)  # Outputs: False")
    input("\nPress Enter to return...")


# conditionals sahsahsadh
def if_elif_else():
    clear()
    print("An if/elif/else statement is used to execute code based on certain conditions.")
    print("Example:")
    print("if x > 0:\n    print('Positive')\nelif x == 0:\n    print('Zero')\nelse:\n    print('Negative')")
    input("\nPress Enter to return...")

def nested():
    clear()
    print("A nested if statement is an if statement inside another if statement.")
    print("Example:")
    print("if x > 0:\n    if x < 10:\n        print('x is a positive single-digit number')")
    input("\nPress Enter to return...")

def combining():
    clear()
    print("Combining conditions involves using logical operators to combine multiple conditions in an if statement.")
    print("Example:")
    print("if x > 0 and x < 10:\n    print('x is a positive single-digit number')")
    input("\nPress Enter to return...")


# Loops drklsadjrlasd
def for_loops():
    clear()
    print("A for loop is used to iterate over a sequence (like a list, tuple, or string).")
    print("Example:")
    print("for i in range(5):\n    print(i)")
    input("\nPress Enter to return...")

def while_loops():
    clear()
    print("1 A while loop is used to repeatedly execute a block of code as long as a condition is true.")
    print("Example:")
    print("i = 0\nwhile i < 5:\n    print(i)\n    i += 1")
    input("\nPress Enter to return...")

def nested_loops():
    clear()
    print("A nested loop is a loop inside another loop.")
    print("Example:")
    print("for i in range(3):\n    for j in range(2):\n        print(i, j)")
    input("\nPress Enter to return...")

def loop_control():
    clear()
    print("Loop control statements are used to control the flow of loops, such as break, continue, and pass.")
    print("Example:")
    print("for i in range(5):\n    if i == 3:\n        break\n    print(i)")
    input("\nPress Enter to return...")


# Lists and functions skdrthnaslkdr
def lists():
    clear()
    print("A list is a collection of items that are ordered and changeable.")
    print("Example:")
    print("my_list = [1, 2, 3, 4, 5]\nprint(my_list)")
    input("\nPress Enter to return...")

def functions():
    clear()
    print("A function is a block of code that performs a specific task and can be reused.")
    print("Example:")
    print("def greet(name):\n    print('Hello, ' + name)\ngreet('Alice')")
    input("\nPress Enter to return...")

def defs():
    clear()
    print("A function definition (def) is used to create a new function.")
    print("Example:")
    print("def greet(name):\n    print('Hello, ' + name)\ngreet('Alice')")
    input("\nPress Enter to return...")

def importing_random():
    clear()
    print("The random module is used to generate random numbers and perform random operations.")
    print("Example:")
    print("import random\nprint(random.randint(1, 10))  # Outputs a random integer between 1 and 10")
    input("\nPress Enter to return...")

def dictionaries():
    clear()
    print("A dictionary is a collection of key-value pairs that are unordered, changeable, and indexed.")
    print("Example:")
    print("my_dict = {'name': 'Alice', 'age': 25}\nprint(my_dict['name'])")
    input("\nPress Enter to return...")
