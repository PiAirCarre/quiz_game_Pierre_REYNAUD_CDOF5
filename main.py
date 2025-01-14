def quiz_game():
    questions = [
        {
            "question": "What is the capital of France?",
            "choices": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "choices": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
            "answer": "B"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "choices": ["A) Atlantic", "B) Indian", "C) Pacific", "D) Arctic"],
            "answer": "C"
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "choices": ["A) Charles Dickens", "B) William Shakespeare", "C) J.K. Rowling", "D) Mark Twain"],
            "answer": "B"
        },
        {
            "question": "What is the smallest prime number?",
            "choices": ["A) 0", "B) 1", "C) 2", "D) 3"],
            "answer": "C"
        }
    ]

    print("Welcome to the Quiz Game!")
    score = 0

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        for choice in q["choices"]:
            print(choice)

        answer = input("Your answer (A, B, C, or D): ").strip().upper()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    print(f"\nYou got {score}/{len(questions)} questions correct.")
    print("Thanks for playing!")

if __name__ == "__main__"
    quiz_game()
