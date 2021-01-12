from quest_one_answer import QuestOneAnswer
from quest_multi_answer import QuestMultiAnswer
from quest_yes_no_answer import QuestYesNo


def build(qtype, qid, priority, topic, question, ans_true, ans_false):
    """
    ============================================================================
     Description: Factory - Build a Quest Sub-Class by given QType.
    ============================================================================
     Arguments:
    ----------------------------------------------------------------------------
        1. qtype : str (Question Type {'ONE', 'MULTI', 'YESNO'}).
        2. qid : str (Question Id).
        3. priority : str (Question Priority {'A', 'B', 'C').
        4. topic : Topic Class (Question Topic).
        5. question : str (Question Content).
        6. ans_true : str (True Answer).
        7. ans_false : str (False Answer).
    ============================================================================
     Return: Quest Sub-Class {QuestOneAnswer, QuestMultiAnswer, QuestYesNoAns).
    ============================================================================
    """
    if qtype == 'ONE':
        return QuestOneAnswer(qid, priority, topic, question,
                              ans_true, ans_false)
    if qtype == 'MULTI':
        return QuestMultiAnswer(qid, priority, topic, question,
                                ans_true, ans_false)
    if qtype == 'YESNO':
        return QuestYesNo(qid, priority, topic, question, ans_true, ans_false)
    return None
