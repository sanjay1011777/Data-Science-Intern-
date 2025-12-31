def calculate_grade(marks):
    if 90 <= marks <= 100:
        return "A", "Excellent! Outstanding performance 🌟"
    elif 80 <= marks <= 89:
        return "B", "Very Good! Keep it up 👍"
    elif 70 <= marks <= 79:
        return "C", "Good job! You can do even better 💪"
    elif 60 <= marks <= 69:
        return "D", "Fair effort. Keep practicing 🙂"
    else:
        return "F", "Don’t give up! Learn and try again 💡"


while True:
    try:
        name = input("Enter student name: ")
        marks = int(input("Enter marks (0-100): "))

        if 0 <= marks <= 100:
            grade, message = calculate_grade(marks)
            break
        else:
            print("❌ Marks must be between 0 and 100.")
    except ValueError:
        print("❌ Please enter a valid number.")

print(f"\n📊 RESULT FOR {name.upper()}:")
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
