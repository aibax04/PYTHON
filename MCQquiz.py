# BUILDING A MULTIPLE CHOICE QUIZ 

from question import question

question_prompt = [
    "what color are apples ?\n (a) red/green\n(b)purple\n(c) orange\n\n" ,
    "what color are bananas ?\n (a) teal\n(b) magenta\n(c)  yellow\n\n",
    "what color are strawberries?\n (a) yellow\n(b) red\n(c) blue\n\n"
]

questions = [
    question(question_prompt[0], "a"),
    question(question_prompt[1], "c"),
    question(question_prompt[2], "b"),
    ]

def run_test (questions) :
    score = 0
    for question in questions :
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print ("you got " + str(score) + "/" + str(len(questions)) +" correct")

run_test(questions)