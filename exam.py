import random
from f_excel.c_excel import Excel
from topics import Topics


path_myq = 'g:\\myq\\'


def run(xls_qs='questions.xlsx'):
    topics = Topics(path_myq)
    if not topics.is_valid:
        return

    print(f'\n\n\n{"="*75}\nStart Exam\n{"="*75}\n')

    """
    qs = list(Quests(xls_qs=xls_qs).qs.values())

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
    """


if __name__ == '__main__':
    run()
