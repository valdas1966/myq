import random


class Quest:
    """
    ============================================================================
     Description: Represent a Question.
    ============================================================================
    """

    # Random List with True and False Answers
    answers = list()

    # Index of True-Answer in the List of Answers
    index_ans_true = 0

    # The Question has only One-Answer (User need to write the full Answer)
    is_one_answer = False

    def __init__(self, qid, topics, question, ans_true, ans_false):
        """
        ========================================================================
         Description: Constructor - Init Attributes.
        ========================================================================
            1. qid : int
            2. topics : list of str
            3. question : str
            4. ans_true : str
            5. ans_false : list of str
        ========================================================================
        """
        assert type(qid) == int
        assert type(topics) == list
        assert type(question) == str
        assert type(ans_true) == str
        assert type(ans_false) == list
        # Question Id
        self.qid = qid
        # Topics of the Question (Main | Sub)
        self.topics = topics
        # Question Text
        self.question = question
        # True Answer Text
        self.ans_true = ans_true
        self.__set_answers(ans_false)
        self.__set_is_one_answer()
        self.__set_index_ans_true()

    def __set_answers(self, ans_false):
        """
        ========================================================================
         Description: Set Private-Attribute to hold Random-List of
                        True and False Answers.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. ans_false : list of str (List of False-Answers).
        ========================================================================
        """
        assert type(ans_false) == list
        # Drop Null False-Answers (Excel Questions may have Nulls False-Answers)
        ans_false = list(filter(None, ans_false))
        self.answers = ans_false + [self.ans_true]
        random.shuffle(self.answers)

    def __set_index_ans_true(self):
        """
        ========================================================================
         Description: Set Private-Attribute to hold the Index of True-Answer
                        in the Answers-List.
        ========================================================================
        """
        self.index_ans_true = 0
        for i in range(1, len(self.answers)):
            if self.answers[i] == self.ans_true:
                self.index_ans_true = i
                break

    def __set_is_one_answer(self):
        """
        ========================================================================
         Description: Set Private-Attribute to hold if the Question has
                        only one True-Answer.
        ========================================================================
        """
        self.is_one_answer = len(self.answers) == 1
