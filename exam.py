import random
from quests import Quests

qs = list(Quests().qs.values())

counter = 1
while True:
    random.shuffle(qs)
    q = qs[0]
    text = f'#{counter}. {q.question}:\n'
    if not q.has_one_answer:
        for j, answer in enumerate(q.answers):
            text += f'\t{j+1}. {answer}\n'
    ans = input(f'{text}-> ')
    if ans == '0':
        break
    counter += 1



