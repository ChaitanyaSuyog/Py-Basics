from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Magenta\n\n",
    "What color are bananas?\n(a) Teal\n(b) Lime\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Blue\n(b) Red\n(c) Black\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You scored " + str(score) + "/" + str(len(questions)) + " correct.")


run_test(questions)
