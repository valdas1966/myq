import random
from quests import Quests


def ask_question(q, counter):
    text = f'{"="*50}\n#{counter}. {q.question}:\n'
    if q.qtype == 'ONE':
        return ask_one_answer_question(q, text)
    if q.qtype == 'YESNO':
        return ask_yes_no_answer_question(q, text)
    return ask_multi_answer_question(q, text)


def ask_one_answer_question(q, text):
    ans = input(text + '-> ')
    # True-Answer
    if ans == q.answer_true:
        log(q, True)
        print('Right Answer!')
        return True
    # Break
    if ans == '0':
        return False
    # False-Answer
    log(q, False, ans)
    print(f'{"="*50}\nThe right answer is: {q.answer_true}')
    return ask_one_answer_question(q, text)


def ask_yes_no_answer_question(q, text):
    ans = input(text + f'(Yes/No):\n-> ')
    # Break
    if ans == '0':
        return False
    if ans in {'1', 'y', 'Y', 'Yes', 'YES', 'yes'}:
        ans = 'Yes'
    elif ans in {'2', 'n', 'N', 'No', 'NO', 'no'}:
        ans = 'No'
    # Illegal-Answer
    if ans not in {'Yes', 'No'}:
        return ask_yes_no_answer_question(q, text)
    # True-Answer
    if ans == q.answer_true:
        log(q, True)
        print('Right Answer!')
        return True
    # False-Answer
    log(q, False, ans)
    print(f'{"=" * 50}\nThe right answer is: {ans}')
    return ask_one_answer_question(q, text)


def ask_multi_answer_question(q, text):
    text_temp = text
    for i, answer in enumerate(q.answers):
        # i+1 because zero-based
        text_temp += f'{i+1}. {answer}\n'
    ans = input(text_temp + '-> ')
    if ans.isnumeric():
        ans = int(ans)
    else:
        ans = -1
    # Break
    if ans == 0:
        return False
    # Illegal-Answer
    if ans not in [i for i in range(len(q.answers) + 1)]:
        return ask_multi_answer_question(q, text)
    # True-Answer (ans-1 because zero-based)
    if q.answers[ans-1] == q.answer_true:
        log(q, True)
        print('Right Answer!')
        return True
    # False-Answer
    # ans-1 because zero-based
    log(q, False, q.answers[ans-1])
    print(f'{"=" * 50}\nThe right answer is: {q.answer_true}')
    q.shuffle_answers()
    return ask_multi_answer_question(q, text)


def log(q, res, ans=None):
    print('log()')


def run_local():
    print(f'\n\n\n{"="*50}\nStart Exam\n{"="*50}\n')

    qs = list(Quests().qs.values())

    counter = 1
    while True:
        random.shuffle(qs)
        q = qs[0]
        # Get Answer to Question
        if ask_question(q, counter):
            counter += 1
        # Break-Command
        else:
            break


def run_colab():
    print(f'\n\n\n{"="*50}\nStart Exam\n{"="*50}\n')

    qs = list(Quests(xls_qs='/content/myq/questions.xlsx').qs.values())

    counter = 1
    while True:
        random.shuffle(qs)
        q = qs[0]
        # Get Answer to Question
        if ask_question(q, counter):
            counter += 1
        # Break-Command
        else:
            break
