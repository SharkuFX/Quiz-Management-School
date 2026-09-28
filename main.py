import pymysql as p
import random as r
password = input("Enter your MySQL password: ")

#Creating a database
def crdb():
    c=p.connect(host='localhost',user='root',password=password,database='')
    cur=c.cursor()
    q="CREATE DATABASE IF NOT EXISTS PROJECT_QUIZ"
    cur.execute(q)
    c.close()
    print("Database created successfully!")
crdb()

#Creating a table
def crtb():
    c=p.connect(host='localhost',user='root',password=password,database='PROJECT_QUIZ')
    cur=c.cursor()
    q="CREATE TABLE IF NOT EXISTS questions (id INT AUTO_INCREMENT PRIMARY KEY, category VARCHAR(255), question TEXT, option1 VARCHAR(255), option2 VARCHAR(255), option3 VARCHAR(255), option4 VARCHAR(255), answer CHAR(1))"
    cur.execute(q)
    c.close()
    print("Table created successfully!")
crtb()

#Inserting default questions into the table
def ins_defq():
    c=p.connect(host='localhost',user='root',password=password,database='PROJECT_QUIZ')
    cur=c.cursor()
    questions = [

("Science", "What is the chemical symbol for Gold?",
 "Ag", "Au", "Fe", "Cu", "B"),

("Geography", "Which is the largest continent in the world?",
 "Africa", "Europe", "Asia", "North America", "C"),

("History", "Who was the first President of India?",
 "Dr. Rajendra Prasad", "Dr. S. Radhakrishnan",
 "Jawaharlal Nehru", "Mahatma Gandhi", "A"),

("Science", "Which planet is known as the Red Planet?",
 "Venus", "Mars", "Jupiter", "Mercury", "B"),

("India", "What is the capital of India?",
 "Mumbai", "New Delhi", "Kolkata", "Chennai", "B"),

("Geography", "Which is the longest river in India?",
 "Yamuna", "Ganga", "Godavari", "Narmada", "B"),

("Science", "What gas do plants absorb during photosynthesis?",
 "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", "C"),

("Sports", "How many players are there in a cricket team?",
 "9", "10", "11", "12", "C"),

("History", "Who founded the Maurya Empire?",
 "Ashoka", "Chandragupta Maurya", "Bindusara",
 "Harshavardhana", "B"),

("World", "Which is the largest ocean in the world?",
 "Atlantic Ocean", "Indian Ocean", "Pacific Ocean",
 "Arctic Ocean", "C"),

("Science", "What is the SI unit of force?",
 "Joule", "Watt", "Newton", "Pascal", "C"),

("India", "Which Indian state is known as the Land of Rising Sun?",
 "Assam", "Arunachal Pradesh", "Sikkim", "Manipur", "B"),

("Geography", "Which is the smallest continent?",
 "Europe", "Australia", "Antarctica", "South America", "B"),

("History", "Who gave the slogan 'Give me blood, and I will give you freedom'?",
 "Mahatma Gandhi", "Subhas Chandra Bose",
 "Bhagat Singh", "Jawaharlal Nehru", "B"),

("Science", "Which organ pumps blood throughout the human body?",
 "Brain", "Liver", "Heart", "Kidney", "C"),

("Sports", "In which sport is the term 'Love' used?",
 "Cricket", "Tennis", "Hockey", "Football", "B"),

("India", "Which is the national animal of India?",
 "Lion", "Elephant", "Bengal Tiger", "Leopard", "C"),

("Geography", "Mount Everest is located in which mountain range?",
 "Alps", "Andes", "Himalayas", "Rockies", "C"),

("Science", "How many bones are there in an adult human body?",
 "196", "206", "216", "226", "B"),

("History", "Who built the Taj Mahal?",
 "Akbar", "Shah Jahan", "Jahangir", "Aurangzeb", "B"),

("World", "Which country is known as the Land of the Rising Sun?",
 "China", "Japan", "South Korea", "Thailand", "B"),

("Science", "What is the hardest natural substance?",
 "Iron", "Diamond", "Gold", "Quartz", "B"),

("India", "Which is the national flower of India?",
 "Rose", "Lotus", "Sunflower", "Jasmine", "B"),

("Sports", "Which country won the first Cricket World Cup in 1975?",
 "Australia", "England", "West Indies", "India", "C"),

("Geography", "Which desert is the largest hot desert in the world?",
 "Gobi", "Sahara", "Thar", "Kalahari", "B"),

("Science", "What is the boiling point of water at sea level?",
 "50°C", "75°C", "100°C", "150°C", "C"),

("History", "Who was known as the Iron Man of India?",
 "Sardar Vallabhbhai Patel", "Bhagat Singh",
 "Lal Bahadur Shastri", "Bal Gangadhar Tilak", "A"),

("India", "Which Indian city is known as the Pink City?",
 "Jaipur", "Jodhpur", "Udaipur", "Bikaner", "A"),

("Science", "Which vitamin is mainly produced in the skin when exposed to sunlight?",
 "Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D", "D"),

("Sports", "How many rings are there in the Olympic logo?",
 "4", "5", "6", "7", "B"),

("Geography", "Which country has the largest population in the world?",
 "India", "China", "USA", "Russia", "A"),

("History", "Who wrote the Indian National Anthem?",
 "Bankim Chandra Chatterjee", "Rabindranath Tagore",
 "Sarojini Naidu", "Subhas Chandra Bose", "B"),

("Science", "What is the nearest star to Earth?",
 "Sirius", "Sun", "Proxima Centauri", "Polaris", "B"),

("India", "Which is the national bird of India?",
 "Sparrow", "Peacock", "Eagle", "Parrot", "B"),

("Geography", "Which is the largest country in the world by area?",
 "Canada", "China", "Russia", "USA", "C"),

("Science", "Which blood group is known as the universal donor?",
 "AB+", "A+", "O-", "B-", "C"),

("Sports", "Who is known as the God of Cricket in India?",
 "Virat Kohli", "Kapil Dev", "Sachin Tendulkar",
 "MS Dhoni", "C"),

("History", "In which year did India gain independence?",
 "1945", "1946", "1947", "1950", "C"),

("Science", "What is the basic unit of life?",
 "Tissue", "Organ", "Cell", "Atom", "C"),

("World", "Which is the largest country in South America?",
 "Argentina", "Brazil", "Chile", "Peru", "B"),

("India", "Which Indian state has the longest coastline?",
 "Kerala", "Gujarat", "Tamil Nadu", "Maharashtra", "B"),

("Science", "Which planet is the largest in our Solar System?",
 "Saturn", "Earth", "Jupiter", "Neptune", "C"),

("History", "Who was the first Prime Minister of independent India?",
 "Sardar Patel", "Jawaharlal Nehru",
 "Rajendra Prasad", "Lal Bahadur Shastri", "B"),

("Sports", "Which sport is associated with Wimbledon?",
 "Football", "Tennis", "Cricket", "Badminton", "B"),

("Geography", "Which line divides the Earth into Northern and Southern Hemispheres?",
 "Prime Meridian", "Equator", "Tropic of Cancer",
 "International Date Line", "B"),

("Science", "What is the chemical formula of water?",
 "CO2", "H2O", "O2", "NaCl", "B"),

("India", "Which is the national fruit of India?",
 "Apple", "Mango", "Banana", "Orange", "B"),

("History", "Who was the first woman Prime Minister of India?",
 "Sarojini Naidu", "Indira Gandhi",
 "Pratibha Patil", "Sushma Swaraj", "B"),

("Sports", "How many players are there in a football team on the field?",
 "9", "10", "11", "12", "C"),

("World", "Which is the largest island in the world?",
 "Greenland", "Madagascar", "Borneo", "New Guinea", "A")

]
    cur.executemany("INSERT INTO questions (category, question, option1, option2, option3, option4, answer) VALUES (%s, %s, %s, %s, %s, %s, %s)", questions)
    c.commit()
    c.close()
    print("Questions inserted successfully!")
ins_defq()

# Inserting a own question into the table
def ins_ownq():
    c=p.connect(host='localhost',user='root',password=password,database='PROJECT_QUIZ')
    cur=c.cursor()
    category = input("Enter the category of the question: ")
    question = input("Enter the question: ")
    option1 = input("Enter option A: ")
    option2 = input("Enter option B: ")
    option3 = input("Enter option C: ")
    option4 = input("Enter option D: ")
    answer = input("Enter the correct answer (A/B/C/D): ")

    cur.execute("INSERT INTO questions (category, question, option1, option2, option3, option4, answer) VALUES (%s, %s, %s, %s, %s, %s, %s)", (category, question, option1, option2, option3, option4, answer))
    c.commit()
    c.close()
    print("Question inserted successfully!")

#displaying questions admin function
def disq():
    c=p.connect(host='localhost',user='root',password=password,database='PROJECT_QUIZ')
    cur=c.cursor()
    cur.execute("SELECT * FROM questions")
    rows = cur.fetchall()
    for row in rows:
        print(f"ID: {row[0]}")
        print(f"Category: {row[1]}")
        print(f"Question: {row[2]}")
        print(f"A: {row[3]}")
        print(f"B: {row[4]}")
        print(f"C: {row[5]}")
        print(f"D: {row[6]}")
        print(f"Answer: {row[7]}")
        print("-----------------------------")
    c.close()

#deleting specific questions admin function
def delq():
    c=p.connect(host='localhost',user='root',password=password,database='PROJECT_QUIZ')
    cur=c.cursor()
    question_id = input("Enter the ID of the question to delete: ")
    cur.execute("DELETE FROM questions WHERE id = %s", (question_id,))
    c.commit()
    c.close()
    print("Question deleted successfully!")

#deleting all questions admin function
def delall():
    c=p.connect(host='localhost',user='root',password=password,database='PROJECT_QUIZ')
    cur=c.cursor()
    cur.execute("TRUNCATE TABLE questions;")
    c.commit()
    c.close()
    print("All questions deleted successfully!")

# ADMINISTRATOR FUNCTION
def admin():
    print("========== ADMIN PANEL ==========\n")
    print("Welcome, Administrator!")
    while True:
        print("\nSelect an option:")
        print("1. Insert Own Question")
        print("2. Display Questions")
        print("3. Delete Question")
        print("4. Delete All Questions")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            ins_ownq()
        elif choice == '2':
            disq()
        elif choice == '3  ':
            delq()
        elif choice == '4':
            delall()
        elif choice == '5':
            print("Exiting Administrator mode.")
            break
        else:
            print("Invalid choice. Please try again.")

#Accesing Admin Panel
def access_admin_panel():
    password = input("Enter the administrator password: ")
    if password == "admin123":
        admin()
    else:
        print("Incorrect password. Access denied.")

# USER FUNCTION
def user():
    c = p.connect(host='localhost', user='root', password=password, database='PROJECT_QUIZ')
    cur = c.cursor()
    w = int(input("Enter the number of questions you want to attempt: "))
    x = input("Enter the category of questions you want to attempt "
              "(Science, Geography, History, India, Sports, World): ")
    cur.execute("SELECT * FROM questions WHERE category = %s", (x,))
    data = cur.fetchall()
    if len(data) < w:
        print("Only", len(data), "questions are available in this category.")
        print("Please enter a smaller number.")
        c.close()
        return
    selected_questions = data[:w]
    score = 0
    for i in range(w):
        question = selected_questions[i]
        print("\n-----------------------------------")
        print("Question", i + 1)
        print("-----------------------------------")
        print("Question:", question[2])
        print("A.", question[3])
        print("B.", question[4])
        print("C.", question[5])
        print("D.", question[6])

        answer = input("Enter your answer A/B/C/D: ").upper()

        if answer == question[7]:
            print("Correct answer!")
            score = score + 4
        else:
            print("Incorrect answer!")
            print("The correct answer is:", question[7])
            score = score - 1

    print("\n-----------------------------------")
    print("You have completed the quiz.")
    print("Your score is:", score, "/", w*4)
    print("Thank you for participating!")
    print("-----------------------------------")

    cur.close()
    c.close()

# MAIN FUNCTION
def main():
    print("========== QUIZ PANEL ==========\n")
    while True:
        print("Select an option:")
        print("1. Administrator")
        print("2. User")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            access_admin_panel()
        elif choice == '2':
            user()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()
