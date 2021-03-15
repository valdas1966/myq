import random
from topics import Topics
from quests import Quests
from f_utils import u_file
from f_utils.c_timer import Timer
from pathlib import Path
from f_logger.tazak import LoggerTazak


path = Path(__file__)
path_myq = str(path.parent)
dir_log = f'{path_myq}\\log'
csv_stat = path_myq + 'stat.csv'


def run():
    topics = Topics(path_myq)
    if not topics.is_valid:
        return
    stat = load_stat()
    quests = Quests(path_myq, topics, stat)

    print(f'\n\n\n{"="*75}\nStart Exam\n{"="*75}\n')
    logger = LoggerTazak()

    counter = 1
    while True:
        q = pick_quest(quests)
        # Get Answer to Question
        ans = q.ask(counter)
        if ans:
        if q.ask(counter, logger):
            counter += 1
            # Update Stats for all other Questions
            for q_other in quests.qs.values():
                if not q_other == q:
                    q_other.last_time += 1
                    q_other.set_grade()
        # Break-Command
        else:
            dump_stat(quests)
            break


def pick_quest(quests):
    """
    ============================================================================
     Description: Create a Bag of Questions (number of occurrences depends on
                    its grade), and return a random question from it.
    ============================================================================
     Arguments:
    ----------------------------------------------------------------------------
        1. quests : Quests-Class (Questions).
    ============================================================================
     Return: Quest-Class (Random Question).
    ============================================================================
    """
    bag = list()
    for qid, q in quests.qs.items():
        bag.extend([qid] * q.grade)
    random.shuffle(bag)
    return quests.qs[bag[0]]


def load_stat():
    """
    ============================================================================
     Description: Load from CSV-File Questions-Statistics and Return as Dict.
    ============================================================================
     Return: Dict of Tuple (asked, answered, last_10, last_time).
    ============================================================================
    """
    stat = dict()
    if not u_file.is_exists(csv_stat):
        return stat
    file = open(csv_stat, 'r')
    lines = file.readlines()
    file.close()
    for line in lines[1:]:
        qid, asked, answered, last_10, last_time = line.strip().split(',')[:-2]
        stat[qid] = (asked, answered, last_10, last_time)
    return stat


def dump_stat(quests):
    """
    ============================================================================
     Description: Dump Question-Statistics into CSV-File.
    ============================================================================
     Arguments:
    ----------------------------------------------------------------------------
        1. quests : Quests-Class (Questions).
    ============================================================================
    """
    file = open(csv_stat, 'w')
    file.write('qid,asked,answered,last_10,last_time,priority_val,grade\n')
    for qid, q in quests.qs.items():
        file.write(f'{qid},{q.asked},{q.answered},{q.last_10},{q.last_time},'
                   f'{q.priority_val},{q.grade}\n')
    file.close()


if __name__ == '__main__':
    run()
