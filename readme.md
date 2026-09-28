# QUIZ MANAGEMENT SYSTEM

## 1. Introduction

The **Quiz Management System** is a Python-based application developed using **Python and MySQL**. The purpose of this project is to create an interactive quiz in which users can attempt a selected number of multiple-choice questions.

The system has two main sections:

1. **Administrator**
2. **User**

The administrator can create the database and table, insert questions, display stored questions, and delete questions. The user can attempt a quiz by selecting the number of questions they want to answer.

The project uses the **PyMySQL library** to establish a connection between Python and the MySQL database.

---

## 2. Objectives of the Project

The main objectives of the Quiz Management System are:

* To create a simple computer-based quiz system.
* To store quiz questions permanently in a MySQL database.
* To provide four options for every question.
* To store the correct answer along with each question.
* To allow the administrator to manage questions.
* To randomly select questions for the user.
* To allow the user to decide how many questions they want to attempt.
* To automatically check whether the user's answer is correct or incorrect.
* To provide a simple and user-friendly menu-driven interface.

---

## 3. Technologies Used

### Python

Python is the main programming language used to develop the application. It is used for creating menus, accepting user input, processing answers, connecting to MySQL, and controlling the overall flow of the program.

### MySQL

MySQL is used as the database management system. It stores the questions, four options, and correct answers.

### PyMySQL

PyMySQL is a Python library that allows Python programs to communicate with a MySQL database. The program imports it using:

```python
import pymysql as p
```

The program also uses Python's `random` module for randomization.

---

## 4. Database Connectivity

The program establishes a connection between Python and MySQL using the `p.connect()` function.

For example:

```python
c = p.connect(
    host='localhost',
    user='root',
    password=password,
    database='PROJECT_QUIZ'
)
```

Here:

* `localhost` represents the computer on which MySQL is running.
* `root` is the MySQL username.
* `password` contains the password entered by the user.
* `PROJECT_QUIZ` is the database used by the application.

After establishing the connection, a **cursor object** is created:

```python
cur = c.cursor()
```

The cursor is used to execute SQL commands from Python.

---

## 5. Creating the Database

The function `crdb()` is responsible for creating the database.

The SQL command used is:

```sql
CREATE DATABASE IF NOT EXISTS PROJECT_QUIZ
```

The `IF NOT EXISTS` clause prevents an error if the database has already been created.

The database is created by executing the SQL query through the cursor:

```python
cur.execute(q)
```

After execution, the database connection is closed.

---

## 6. Creating the Questions Table

The function `crtb()` creates the table named `questions`.

The table contains the following fields:

| Field      | Purpose                      |
| ---------- | ---------------------------- |
| `id`       | Unique identification number |
| `question` | Stores the question          |
| `option1`  | First option                 |
| `option2`  | Second option                |
| `option3`  | Third option                 |
| `option4`  | Fourth option                |
| `answer`   | Stores the correct option    |

The `id` field uses `AUTO_INCREMENT` and is defined as the `PRIMARY KEY`. This means that every question automatically receives a unique ID.

The question itself is stored using the `TEXT` data type, while the options are stored using `VARCHAR(255)`. The correct answer is stored as a single character using `CHAR(1)`.

---

## 7. Inserting Questions

The function `insq()` is used to insert questions into the database.

The questions are first stored in a Python list. Each question contains:

* Question
* Option 1
* Option 2
* Option 3
* Option 4
* Correct answer

For example:

```python
(
    "What is the capital of India?",
    "Mumbai",
    "New Delhi",
    "Kolkata",
    "Chennai",
    "B"
)
```

The `executemany()` function is then used to insert multiple questions into the database at once.

```python
cur.executemany(
    "INSERT INTO questions
    (question, option1, option2, option3, option4, answer)
    VALUES (%s, %s, %s, %s, %s, %s)",
    questions
)
```

## Using `executemany()` makes it easier and faster to insert a large number of questions.

## 8. Displaying Questions

The function `dq()` is used by the administrator to display all questions stored in the database.

The SQL command:

```sql
SELECT * FROM questions
```

retrieves all records from the table.

The `fetchall()` method stores all retrieved records:

```python
rows = cur.fetchall()
```

A `for` loop is then used to display every question and its corresponding options and answer.

---

## 9. Deleting a Question

The function `delq()` allows the administrator to delete a particular question.

First, the administrator enters the ID of the question:

```python
question_id = input("Enter the ID of the question to delete: ")
```

The SQL command used is:

```sql
DELETE FROM questions WHERE id = %s
```

The `%s` placeholder is used to pass the ID safely to the SQL query.

After deletion, `commit()` is used to permanently save the change to the database.

---

## 10. Administrator Panel

The administrator panel provides different options for managing the quiz database.

The available options are:

1. Create Database
2. Create Table
3. Insert Questions
4. Display Questions
5. Delete Question
6. Exit

The `admin()` function uses a `while True` loop to continuously display the administrator menu until the administrator selects the Exit option.

An `if-elif` structure is used to identify the administrator's choice and call the corresponding function.

---

## 11. Administrator Password Protection

The administrator panel is protected using a password.

The function `access_admin_panel()` asks the user to enter an administrator password.

If the entered password matches the stored password, the administrator panel is opened:

```python
if password == "admin123":
    admin()
```

Otherwise, access is denied.

This prevents ordinary users from accessing the question-management functions.

---

## 12. User Quiz Module

The `user()` function is responsible for conducting the quiz.

First, the user is asked how many questions they want to attempt:

```python
w = int(input("Enter the number of questions you want to attempt: "))
```

A `for` loop is then used to repeat the quiz process according to the number entered by the user.

For each question, the program retrieves a random question from the database and displays its four options.

---

## 13. Random Question Selection

The program uses the MySQL command:

```sql
SELECT * FROM testquiz
ORDER BY RAND()
LIMIT 1
```

`ORDER BY RAND()` randomizes the order of the records, while `LIMIT 1` selects only one record.

Therefore, the program can obtain a random question from the database.

The selected record is retrieved using:

```python
data = cur.fetchone()
```

The different values can then be accessed using indexes such as:

```python
data[1]    # Question
data[2]    # Option A
data[3]    # Option B
data[4]    # Option C
data[5]    # Option D
data[6]    # Correct answer
```

---

## 14. Answer Checking

After displaying the question and four options, the program accepts the user's answer:

```python
answer = input().upper()
```

The `upper()` function converts the input into uppercase so that answers such as `a` and `A` can be treated in the same way.

The user's answer is compared with the correct answer stored in the database:

```python
if answer == data[6]:
    print("Correct answer!")
else:
    print("Incorrect answer!")
```

If the answer is incorrect, the program also displays the correct answer.

---

## 15. Main Function

The `main()` function controls the overall application.

It provides three choices:

1. Administrator
2. User
3. Exit

The administrator option calls:

```python
access_admin_panel()
```

The user option calls:

```python
user()
```

The program continues to display the main menu using a `while True` loop until the user selects Exit.

---

## 16. Python Concepts Used

The project demonstrates several important Python concepts:

### Functions

Functions such as `crdb()`, `crtb()`, `insq()`, `dq()`, `delq()`, `admin()`, `user()`, and `main()` divide the program into smaller and manageable sections.

### Loops

`while` and `for` loops are used to repeatedly display menus and conduct multiple questions.

### Conditional Statements

`if`, `elif`, and `else` statements are used for menu selection, password verification, and answer checking.

### Lists

A list is used to store multiple questions before inserting them into the database.

### Tuples

Each question in the question list is represented as a tuple containing the question, four options, and the correct answer.

### Input and Output

The `input()` function accepts information from the user, while `print()` displays information on the screen.

---

## 17. SQL Concepts Used

The project uses several SQL commands:

### CREATE DATABASE

Used to create the quiz database.

### CREATE TABLE

Used to create the `questions` table.

### INSERT

Used to add questions to the database.

### SELECT

Used to retrieve questions from the database.

### DELETE

Used to remove a particular question.

### ORDER BY RAND()

Used to randomize the order of questions.

### LIMIT

Used to restrict the number of records returned.

---

## 18. Advantages of the System

* Easy to use.
* Questions are stored permanently in a database.
* Administrator can manage questions.
* Random questions make the quiz more interesting.
* User can choose the number of questions.
* Automatic answer checking saves time.
* Python and MySQL provide a simple combination for developing the application.
* The system can be expanded with additional features in the future.

---

## 19. Limitations

The current version of the system has some limitations:

* Users do not have individual accounts.
* There is no score history.
* The question selection can potentially repeat questions because a random question is selected independently for each attempt.
* The administrator password is directly present in the program.
* There is no graphical user interface.
* There is no timer for each question.
* There is no option for different subjects or difficulty levels.

These limitations provide opportunities for future improvements.

---

## 20. Future Scope

The Quiz Management System can be further improved by adding:

* User registration and login.
* Score tracking.
* Leaderboard.
* Timer for each question.
* Different difficulty levels.
* Subject-wise quizzes.
* Chapter-wise quizzes.
* Lifelines such as 50-50 and audience poll.
* Sound effects and background music.
* Graphical user interface using Tkinter.
* Quiz history stored in MySQL.
* Automatic score calculation.
* Unique random questions without repetition.
* Administrator options for editing and updating questions.

---

## 21. Conclusion

The Quiz Management System demonstrates how **Python programming and MySQL database management** can be combined to develop a practical application.

The project uses Python for the application logic and PyMySQL for communication with the MySQL database. The administrator can create and manage the quiz database, while users can attempt randomly selected multiple-choice questions.

The project provides practical knowledge of **Python functions, loops, conditional statements, lists, tuples, SQL queries, database connectivity, and menu-driven programming**.

Overall, the project is a simple but effective implementation of a computerized quiz system and provides a strong foundation for developing more advanced quiz applications in the future.
