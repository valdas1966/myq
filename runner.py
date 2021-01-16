import random
from f_excel.c_excel import Excel
from topics import Topics
from quests import Quests


path_myq = 'g:\\myq\\'


def run():
    topics = Topics(path_myq)
    if not topics.is_valid:
        return
    quests = Quests(path_myq, topics)

    print(f'\n\n\n{"="*75}\nStart Exam\n{"="*75}\n')

    qs = list(quests.qs.values())

    counter = 1
    while True:
        random.shuffle(qs)
        q = qs[0]
        # Get Answer to Question
        if q.ask(counter):
            counter += 1
        # Break-Command
        else:
            break


if __name__ == '__main__':
    run()
