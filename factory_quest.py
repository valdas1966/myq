from quest_one_answer import QuestOneAnswer
from quest_multi_answer import QuestMultiAnswer
from quest_yes_no_answer import QuestYesNo


def build(qtype, qid, row, priority, topic, question,
          ans_true, ans_false, img, df_logger):
    """
    ============================================================================
     Description: Factory - Build a Quest Sub-Class by given QType.
    ============================================================================
     Arguments:
    ----------------------------------------------------------------------------
        1. qtype : str (Question Type {'ONE', 'MULTI', 'YESNO'}).
        2. qid : int (Question Id).
        3. row : int (Row in Excel - for Ordering).
        4. priority : str (Question Priority {'A', 'B', 'C').
        5. topic : Topic Class (Question Topic).
        6. question : str (Question Content).
        7. ans_true : str (True Answer).
        8. ans_false : str (False Answer).
        9. img : str (Path to Image).
        10. df_logger : DataFrame
    ============================================================================
     Return: Quest Sub-Class {QuestOneAnswer, QuestMultiAnswer, QuestYesNoAns).
    ============================================================================
    """
    if qtype == 'ONE':
        return QuestOneAnswer(qid, row, priority, topic, question,
                              ans_true, ans_false, img, df_logger)
    if qtype == 'MULTI':
        return QuestMultiAnswer(qid, row, priority, topic, question,
                                ans_true, ans_false, img, df_logger)
    if qtype == 'YESNO':
        return QuestYesNo(qid, row, priority, topic, question,
                          ans_true, ans_false, img, df_logger)
    return None
