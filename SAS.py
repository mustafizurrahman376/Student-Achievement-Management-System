class Student:
    def __init__(self, ID, name, gender, age, math_score, english_score, computer_score):
        self.ID = ID
        self.name = name
        self.gender = gender
        self.age = age
        self.math_score = math_score
        self.english_score = english_score
        self.computer_score = computer_score

students = []

def InputAchievement():
    ID = input("Enter student ID: ")
    name = input("Enter student name: ")
    gender = input("Enter student gender: ")
    age = int(input("Enter student age: "))
    math_score = float(input("Enter Math score: "))
    english_score = float(input("Enter English score: "))
    computer_score = float(input("Enter Computer score: "))
    student = Student(ID, name, gender, age, math_score, english_score, computer_score)
    students.append(student)

def OutputAchievement():
    for student in students:
        print("ID:", student.ID)
        print("Name:", student.name)
        print("Gender:", student.gender)
        print("Age:", student.age)
        print("Math score:", student.math_score)
        print("English score:", student.english_score)
        print("Computer score:", student.computer_score)
        print("")

def QueryScoresByID(ID):
    for student in students:
        if student.ID == ID:
            return student.math_score, student.english_score, student.computer_score
    return None

def QueryScoresByName(name):
    for student in students:
        if student.name == name:
            return student.math_score, student.english_score, student.computer_score
    return None

def UpdateAchievementByID(ID):
    for student in students:
        if student.ID == ID:
            print("Student Found By ID.")
            student.math_score = float(input("Enter updated Math score: "))
            student.english_score = float(input("Enter updated English score: "))
            student.computer_score = float(input("Enter updated Computer score: "))
            return
    print("Student not found.")

def UpdateAchievementByName(name):
    for student in students:
        if student.name == name:
            print("Student Found By Name.")
            student.math_score = float(input("Enter updated Math score: "))
            student.english_score = float(input("Enter updated English score: "))
            student.computer_score = float(input("Enter updated Computer score: "))
            return
    print("Student not found.")

def ComputeTotalAndAverageScores():
    for student in students:
        total_score = student.math_score + student.english_score + student.computer_score
        average_score = total_score / 3
        print("ID:", student.ID)
        print("Name:", student.name)
        print("Total score:", total_score)
        print("Average score:", average_score)
        print("")

# Example usage
InputAchievement()
OutputAchievement()
UpdateAchievementByID("1")
OutputAchievement()
UpdateAchievementByName("Johndoe")
OutputAchievement()
ComputeTotalAndAverageScores()