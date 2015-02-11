"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["404"],
            "answer": True
        },
        {
            "input": ["Palindrome"],
            "answer": False
        },
        {
            "input": ["Amor, Roma"],
            "answer": True
        }
    ],
    "Extra": [
        {
            "input":["No 'x' in Nixon"],
            "answer": True
        },
        {
            "input": ["A Man, A Plan, A Canal, Panama"],
            "answer": True
        },
        {
            "input": ["Lorem Ipsum is simply dummy text of the printing and typesetting industry."],
            "answer": False
        }
    ]
}


