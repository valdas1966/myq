import random
from quests import Quests

def ask_question(q):
    text = f'#{counter}. {q.question}:\n'
    if q.has_one_answer:
        ask_one_answer_question(q)


def ask_one_answer_question(q):


qs = list(Quests().qs.values())

counter = 1
while True:
    random.shuffle(qs)
    q = qs[0]

    if not q.has_one_answer:
        for j, answer in enumerate(q.answers):
            text += f'\t{j+1}. {answer}\n'
    ans = input(f'{"="*50}\n{text}-> ')
    if ans == '0':
        break
    counter += 1



