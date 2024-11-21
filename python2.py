import os

# File to store user data
user_data_file = "user_data.txt"


def register():
    enroll = input("Enter enrollment number: ")
    password = input("Enter the password: ")
    with open(user_data_file, "a") as file:
        file.write(f"{enroll},{password}\n")
    print("Registration successful!")


def check(enroll, password):
    if not os.path.exists(user_data_file):
        return False

    with open(user_data_file, "r") as file:
        for line in file:
            stored_enroll, stored_password = line.strip().split(",")
            if enroll == stored_enroll and password == stored_password:
                return True
    return False


def login():
    enroll = input("Enter enrollment number: ")
    password = input("Enter password: ")
    if check(enroll, password):
        print(f"Welcome {enroll}")
        return True
    else:
        print("Not present in register.")
        return False


def quiz_database():
    print("Welcome to the Database Quiz!")
    result = 0  # Initialize the result score

    questions = [
        ("1. Which of the following is a primary key?", "a", ["a) Unique key", "b) Foreign key", "c) Composite key", "d) Primary key"]),
        ("2. What does SQL stand for?", "a", ["a) Structured Query Language", "b) Simple Query Language", "c) Structured Question Language", "d) Simple Question Language"]),
        ("3. Which of the following is NOT a database management system?", "d", ["a) MySQL", "b) Oracle", "c) MS Access", "d) HTML"]),
        ("4. What is a foreign key used for?", "b", ["a) To uniquely identify records", "b) To link two tables together", "c) To index database fields", "d) None of the above"]),
        ("5. What is the command to create a table in SQL?", "a", ["a) CREATE TABLE", "b) ADD TABLE", "c) MAKE TABLE", "d) NEW TABLE"]),
    ]

    for q, correct, options in questions:
        print(q)
        for option in options:
            print(option)
        answer = input("Enter your answer (a/b/c/d): ")
        if answer == correct:
            result += 1

    print(f"Your total score is: {result} out of {len(questions)}")
    return result


def quiz_dsa():
    print("Welcome to the DSA Quiz!")
    result = 0

    questions = [
        ("1. What is the time complexity of binary search?", "a", ["a) O(log n)", "b) O(n)", "c) O(n^2)", "d) O(1)"]),
        ("2. Which data structure uses FIFO principle?", "a", ["a) Queue", "b) Stack", "c) Tree", "d) Graph"]),
    ]

    for q, correct, options in questions:
        print(q)
        for option in options:
            print(option)
        answer = input("Enter your answer (a/b/c/d): ")
        if answer == correct:
            result += 1

    print(f"Your total score is: {result} out of {len(questions)}")
    return result


def quiz_python():
    print("Welcome to the Python Quiz!")
    result = 0

    questions = [
        ("1. What is the output of 3 + 2 * 2 in Python?", "c", ["a) 10", "b) 12", "c) 7", "d) 8"]),
        ("2. Which of the following is used to define a function in Python?", "a", ["a) def", "b) function", "c) fun", "d) func"]),
    ]

    for q, correct, options in questions:
        print(q)
        for option in options:
            print(option)
        answer = input("Enter your answer (a/b/c/d): ")
        if answer == correct:
            result += 1

    print(f"Your total score is: {result} out of {len(questions)}")
    return result


# Initial user interaction
if login():
    print("Welcome to the Quiz Platform!")
else:
    j = int(input("Click 1 to register or 2 to exit: "))
    if j == 1:
        register()
        if login():
            print("Welcome to the Quiz Platform!")
        else:
            print("Invalid login attempt after registration.")
    else:
        print("Thank you for visiting.")
        exit()

# Quiz Section
print("Attempt Quiz: 1 for Database, 2 for DSA, and 3 for Python")
it = int(input("Enter the number: "))

if it == 1:
    result = quiz_database()
    print(f"Your result is: {result}")
elif it == 2:
    result = quiz_dsa()
    print(f"Your result is: {result}")
elif it == 3:
    result = quiz_python()
    print(f"Your result is: {result}")
else:
    print("Invalid choice!")