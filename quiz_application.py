# quiz_app# Quiz Application
# Developed by T Manoj Kumar

score = 0

questions = [
    {
        "question": "What is the capital of India?",
        "answer": "delhi"
    },
    {
        "question": "Which language is used for programming?",
        "answer": "python"
    },
    {
        "question": "What does CPU stand for?",
        "answer": "central processing unit"
    },
    {
        "question": "What is 5 + 5?",
        "answer": "10"
    }
]

print("Welcome to Quiz Application")
print("---------------------------")

for q in questions:
    user_answer = input(q["question"] + ": ").lower()

    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong answer\n")

print("Quiz completed")
print("Your score is:", score, "/", len(questions))lication.py
