import random
from topics import Topics
from quests import Quests
from exam import Exam
from db import DB
from f_utils import u_file
from pathlib import Path
from f_logger.tazak import LoggerTazak


path = Path(__file__)
path_myq = f'{str(path.parent)[0]}:\\myq'
dir_logger = f'{path_myq}\\logs'
csv_stat = f'{path_myq}\\stat.csv'


def run():
    topics = Topics(path_myq)
    if not topics.is_valid:
        return

    stat = load_stat()
    titles_logger = ['qid', 'question', 'asked', 'answered',
                     'last_10', 'last_time', 'priority_val', 'grade', 'ans',
                     'is_true', 'elapsed']
    logger = LoggerTazak(titles_logger, dir_logger)
    exam = Exam(path_myq)

    print(f'\n\n\n{"="*75}\nStart Exam\n{"="*75}\n')

    counter = 1
    for (name_topic, size) in exam.ordered_topics:
        node_topic = topics.tree.nodes[name_topic]
        subtree = topics.tree.subtree(node_topic)
        quests = Quests(path_myq, subtree, stat, logger)
        for i in range(size):
            q = pick_quest(quests)
            # Get Answer to Question
            if q.ask(counter):
                counter += 1
                # Update Stats for all other Questions
                for q_other in quests.qs.values():
                    if not q_other == q:
                        q_other.last_time += 1
                        q_other.set_grade()
            # Break-Command
            else:
                dump_stat(quests)
                logger.close()
                return


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
        if not q.topic:
            continue
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
        qid = int(qid)
        asked = int(asked)
        answered = int(answered)
        last_time = int(last_time)
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
        file.write(f'{qid},{q.asked},{q.answered},{q.last_10}'
                   f',{q.last_time},'
                   f'{q.priority_val},{q.grade}\n')
    file.close()


if __name__ == '__main__':
    run()
