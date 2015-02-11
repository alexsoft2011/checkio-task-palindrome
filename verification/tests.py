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
            "input": [404],
            "answer": True,
            "explanation": "404=?"
        },
        {
            "input": [Palindrome],
            "answer": False,
            "explanation": "Palindrome=?"
        },
        {
            "input": [Amor, Roma],
            "answer": True,
            "explanation": "Amor, Roma=?"
        }
    ],
    "Extra": [
        {
            "input": [No 'x' in Nixon],
            "answer": True,
            "explanation": "No 'x' in Nixon=?"
        },
        {
            "input": [A Man, A Plan, A Canal, Panama],
            "answer": True,
            "explanation": "A Man, A Plan, A Canal, Panama=?"
        }
    ]
}
