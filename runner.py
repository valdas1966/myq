import random
import pandas as pd
from topics import Topics
from quests import Quests
from exam import Exam
from db import DB
from pathlib import Path


path = Path(__file__)
path_myq = f'{str(path.parent)[0]}:\\myq'
dir_logger = f'{path_myq}\\logs'
csv_stat = f'{path_myq}\\stat.csv'


def run():
    topics = Topics(path_myq)
    if not topics.is_valid:
        return
    quests = Quests(path_myq, topics.tree)
    db = DB(path_myq)
    db.open()
    quests.load_stat(db.get_stat())
    db.close()
    exam = Exam(path_myq)

    print(f'\n\n\n{"="*75}\nStart Exam\n{"="*75}\n')

    counter = 1
    for (name_topic, size) in exam.ordered_topics:
        node_topic = topics.tree.nodes[name_topic]
        subtree = topics.tree.subtree(node_topic)
        for i in range(size):
            q = pick_quest(quests, subtree)
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
                df_stat = quests.to_df_stat()
                df_logger = quests.to_df_logger()
                db.open()
                db.update_stat(df_stat)
                db.update_logger(df_logger)
                db.close()
                return


def pick_quest(quests, tree_topics):
    """
    ============================================================================
     Description: Create a Bag of Questions (number of occurrences depends on
                    its grade), and return a random question from it.
    ============================================================================
     Arguments:
    ----------------------------------------------------------------------------
        1. quests : Quests-Class (Questions).
        2. tree_topics : Tree of Topics
    ============================================================================
     Return: Quest-Class (Random Question).
    ============================================================================
    """
    random.seed(random.randint(1, 100))
    bag = list()
    for qid, q in quests.qs.items():
        if q.topic.name not in tree_topics.nodes:
            continue
        bag.extend([qid] * q.grade)
    random.shuffle(bag)
    return quests.qs[bag[0]]


if __name__ == '__main__':
    run()
