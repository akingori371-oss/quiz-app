questions = [
    {
        "question": "What is the capital of Kenya?",
        "choices": {
            "A": "Mombasa",
            "B": "Nairobi",
            "C": "Kisumu",
            "D": "Nakuru"
        },
        "answer": "B"
    },

    {
        "question": "What is 5 + 3?",
        "choices": {
            "A": "6",
            "B": "7",
            "C": "8",
            "D": "9"
        },
        "answer": "C"
    },

    {
        "question": "Which programming language are you learning?",
        "choices": {
            "A": "Java",
            "B": "C++",
            "C": "Python",
            "D": "Ruby"
        },
        "answer": "C"
    },

    {
        "question": "What type of data is 'Hello'?",
        "choices": {
            "A": "int",
            "B": "str",
            "C": "float",
            "D": "bool"
        },
        "answer": "B"
    },

    {
        "question": "Which keyword creates a function in Python?",
        "choices": {
            "A": "function",
            "B": "func",
            "C": "def",
            "D": "create"
        },
        "answer": "C"
    },

    {
        "question": "Which symbol is used for multiplication?",
        "choices": {
            "A": "+",
            "B": "*",
            "C": "/",
            "D": "%"
        },
        "answer": "B"
    },

    {
        "question": "Which function gets input from the user?",
        "choices": {
            "A": "get()",
            "B": "input()",
            "C": "read()",
            "D": "user()"
        },
        "answer": "B"
    }
]
total = 0

for item in questions:
    print(item["question"])
    print(item["choices"])

    ques = input("Your answer: ")

    if ques == item["answer"]:
        total += 1
        print("Correct")

    else:
        print("Your answer is wrong sadly")
        
    
        print("Your final score" ,total)
        
  