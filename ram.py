def quiz_database():
    print("Welcome to the Database Quiz!")
    result = 0  # Initialize the result score

    questions = [
        ("1. Which of the following is a primary key?", "a", ["a) Unique key", "b) Foreign key", "c) Composite key", "d) Primary key"]),
        ("2. What does SQL stand for?", "a", ["a) Structured Query Language", "b) Simple Query Language", "c) Structured Question Language", "d) Simple Question Language"]),
        ("3. Which of the following is NOT a database management system?", "d", ["a) MySQL", "b) Oracle", "c) MS Access", "d) HTML"]),
        ("4. What is a foreign key used for?", "b", ["a) To uniquely identify records", "b) To link two tables together", "c) To index database fields", "d) None of the above"]),
        # Add 16 more questions below:
        ("5. What is the command to create a table in SQL?", "a", ["a) CREATE TABLE", "b) ADD TABLE", "c) MAKE TABLE", "d) NEW TABLE"]),
        ("6. What is a stored procedure?", "c", ["a) A type of database", "b) A database table", "c) A function stored in a database", "d) A query result"]),
        ("7. What does ACID stand for in databases?", "b", ["a) Automated, Consistent, Informative, Durable", "b) Atomicity, Consistency, Isolation, Durability", "c) Accuracy, Clarity, Integrity, Durability", "d) None of the above"]),
        ("8. What is normalization in a database?", "d", ["a) Dividing the database", "b) Combining the database", "c) Creating backups", "d) Organizing data to reduce redundancy"]),
        ("9. Which SQL clause is used to sort results?", "c", ["a) SORT", "b) ORDER", "c) ORDER BY", "d) ARRANGE"]),
        ("10. What is an index in a database?", "d", ["a) A backup table", "b) A log file", "c) A search tool", "d) A performance improvement structure"]),
        ("11. What is the default port number for MySQL?", "c", ["a) 8080", "b) 443", "c) 3306", "d) 1521"]),
        ("12. What does DML stand for?", "a", ["a) Data Manipulation Language", "b) Data Modification Language", "c) Data Mapping Language", "d) Data Merging Language"]),
        ("13. Which of the following is NOT a valid SQL command?", "d", ["a) SELECT", "b) INSERT", "c) DELETE", "d) JOINED"]),
        ("14. What is a transaction in databases?", "a", ["a) A series of operations treated as a single unit", "b) A stored procedure", "c) A backup", "d) A query"]),
        ("15. What does JOIN in SQL do?", "b", ["a) Sorts data", "b) Combines rows from two or more tables", "c) Deletes duplicates", "d) None of the above"]),
        ("16. What is a deadlock?", "d", ["a) A failure in data insertion", "b) A backup error", "c) When two queries are executed at the same time", "d) When two or more processes wait for each other to release resources"]),
        ("17. What does the SQL command 'TRUNCATE' do?", "c", ["a) Deletes the database", "b) Deletes specific rows", "c) Removes all rows from a table", "d) Adds a column"]),
        ("18. What is a cursor in SQL?", "a", ["a) A database object used to retrieve data", "b) A query optimizer", "c) An index", "d) None of the above"]),
        ("19. What is a trigger in SQL?", "b", ["a) A data integrity rule", "b) A set of SQL statements automatically executed", "c) A table relationship", "d) A stored procedure"]),
        ("20. What is SQL injection?", "c", ["a) A way to secure the database", "b) A way to optimize queries", "c) A code injection technique", "d) None of the above"])
    ]

    for q, correct, options in questions:
        print(q)
        for option in options:
            print(option)
        answer = input("Enter your answer (a/b/c/d): ")
        if answer == correct:
            result += 1  # Increment the result if the answer is correct

    print(f"Your total score is: {result} out of 20")
    return result


def quiz_dsa():
    print("Welcome to the DSA Quiz!")
    result = 0  # Initialize the result score

    questions = [
        ("1. What is the time complexity of binary search?", "a", ["a) O(log n)", "b) O(n)", "c) O(n^2)", "d) O(1)"]),
        # Add 19 more questions in a similar format below:
        ("2. Which data structure uses FIFO principle?", "a", ["a) Queue", "b) Stack", "c) Tree", "d) Graph"]),
        ("3. What is the time complexity of quicksort in the worst case?", "c", ["a) O(log n)", "b) O(n)", "c) O(n^2)", "d) O(n log n)"]),
        ("4. Which of the following is a non-linear data structure?", "b", ["a) Array", "b) Tree", "c) Stack", "d) Queue"]),
        ("5. In a linked list, each element is called?", "c", ["a) Node", "b) Link", "c) Element", "d) Component"]),
        # Add more...
    ]

    for q, correct, options in questions:
        print(q)
        for option in options:
            print(option)
        answer = input("Enter your answer (a/b/c/d): ")
        if answer == correct:
            result += 1

    print(f"Your total score is: {result} out of 20")
    return result


def quiz_python():
    print("Welcome to the Python Quiz!")
    result = 0  # Initialize the result score

    questions = [
        ("1. What is the output of 3 + 2 * 2 in Python?", "c", ["a) 10", "b) 12", "c) 7", "d) 8"]),
        # Add 19 more questions in a similar format below:
        ("2. Which of the following is used to define a function in Python?", "a", ["a) def", "b) function", "c) fun", "d) func"]),
        ("3. What is the output of the expression: len([1, 2, 3])?", "c", ["a) 1", "b) 2", "c) 3", "d) 4"]),
        ("4. What data type is the object below? x = 'Hello World'", "a", ["a) str", "b) list", "c) tuple", "d) dict"]),
        # Add more...
    ]

    for q, correct, options in questions:
        print(q)
        for option in options:
            print(option)
        answer = input("Enter your answer (a/b/c/d): ")
        if answer == correct:
            result += 1

    print(f"Your total score is: {result} out of 20")
    return result


def register(dict1):
    enroll = input("Enter enrollment number: ")
    password = input("Enter the password: ")
    dict1[enroll] = password  # Register the enrollment and password


def check(enroll, password, dict1):
    for key, val in dict1.items():
        if key == enroll and val == password:
            return True
    return False


def login(enroll, password):
    if check(enroll, password, dict1):
        print(f"Welcome {enroll}")
        return True
    else:
        print("Not present in register.")
        return False


# Initialize the dictionary
dict1 = {}

# Prompt for initial login attempt
enroll = input("Enter enrollment number: ")
password = input("Enter password: ")

if login(enroll, password):
    print("Welcome")
else:
    j = int(input("Click 1 to register or 2 to exit: "))
    if j == 1:
        # Register a new user
        register(dict1)
        while True:
            i = int(input("Click 1 to login or 2 to exit: "))
            if i == 1:
                enroll = input("Enter enrollment number: ")
                password = input("Enter password: ")
                if login(enroll, password):
                    print("Welcome")
                    break  # Exit the loop on successful login
                else:
                    k = int(input("1 to try again or 0 to exit: "))
                    if k == 1:
                        continue  # Retry login
                    else:
                        break  # Exit the loop if the user chooses to exit
            else:
                print("Thank you for visiting")
                break
    else:
        print("Thank you for visiting.")

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