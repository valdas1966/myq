import random
from topics import Topics
from quests import Quests
from exam import Exam
from db import DB
import utils.path_myq


path_myq = utils.path_myq.get()
dir_logger = f'{path_myq}\\logs'
csv_stat = f'{path_myq}\\stat.csv'


def run():
    topics = Topics(path_myq)
    if not topics.is_valid:
        return
    quests = Quests(path_myq, topics.tree)
    quests.load_stat(DB.get_stat())
    exam = Exam(path_myq)

    print(f'\n\n\n{"="*75}\nStart Exam\n{"="*75}\n')

    is_break = False
    counter = 1
    for (name_topic, size) in exam.ordered_topics:
        if is_break:
            break
        node_topic = topics.tree.nodes[name_topic]
        subtree = topics.tree.subtree(node_topic)
        li_q = pick_quests(quests, subtree, size)
        for q in li_q:
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
                is_break = True
                break
    df_stat = quests.to_df_stat()
    df_logger = quests.to_df_logger()
    DB.update(df_stat, df_logger)


def pick_quests(quests, tree_topics, size):
    """
    ============================================================================
     Description: Create a Bag of Questions (number of occurrences depends on
                    its grade), and returns random questions from it.
    ============================================================================
     Arguments:
    ----------------------------------------------------------------------------
        1. quests : Quests-Class (Questions).
        2. tree_topics : Tree of Topics.
    ============================================================================
     Return: list of quest (Quest-Class).
    ============================================================================
    """
    random.seed(random.randint(1, 100))
    bag = list()
    for qid, q in quests.qs.items():
        if q.topic.name not in tree_topics.nodes:
            continue
        bag.extend([qid] * q.grade)
    random.shuffle(bag)
    set_q = set()
    while len(set_q) < size:
        set_q.add(quests.qs[bag.pop()])
    return sorted(set_q)


if __name__ == '__main__':
    run()
