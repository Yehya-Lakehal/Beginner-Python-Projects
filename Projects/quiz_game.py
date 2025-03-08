# Python Quiz Game

print("====================================")
print("Welcome To My Quiz Game!")

questions = ("What company was initially known as \"Blue Ribbon Sports\"?",
             "How many bones do we have in an ear?",
             "What is the chemical element with the symbol Fe?",
             "What is the smallest unit of matter?",
             "Where did sushi originate? ")

options = (("a- Adidas", "b- Nike", "c- Lacoste"),
           ("a- 9", "b- 2", "c- 3 "),
           ("a- Iron", "b- Fluorine", "c- Silver"),
           ("a- Electron", "b- Proton", "c- Atom"),
           ("a- China", "b- South Korea", "c- Japan"))

answers = ("b","b","a","c","c")

correct_answers = 0

for i in questions:
    print(i)
    print(f"    - {options[questions.index(i)][0]}, {options[questions.index(i)][1]}, {options[questions.index(i)][2]}")
    answer = input("Enter your Answer(a, b or c): ").lower()
    if answer == answers[questions.index(i)]:
        correct_answers += 1
    print("    ============================    ")

print(f"Your Correct Answers: {correct_answers}")

print("====================================")
