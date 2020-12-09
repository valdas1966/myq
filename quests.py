from f_excel.c_excel import Excel
from quest import Quest


class Quests:
    """
    ============================================================================
     Description: Represents Questions Data-Structure.
    ============================================================================
    """

    # First Row in xls_qs
    fr = 2
    # First Col in xls_qs
    fc = 1
    # Last Col in xls_qs
    lc = 9

    # ===================
    # Excel Columns
    # ===================
    # Question Id
    col_qid = 1
    # Is Valid Question (1/0)
    col_valid = 2
    # Priority of the Question
    col_priority = 3
    # First Topic-Column
    col_topic_first = 4
    # Last Topic-Column
    col_topic_last = 5
    # Text of the Question
    col_question = 6
    # Text of the True-Answer
    col_answer_true = 7
    # First False-Answer Column
    col_answer_false_first = 8
    # Last False-Answer Column
    col_answer_false_last = 10
    # Date Created
    col_date_created = 11

    # Dict of Questions {int (Qid) -> Quest (Question)}
    qs = dict()

    def __init__(self, xls_qs='questions.xlsx'):
        """
        ========================================================================
         Description: Constructor. Init the Dict of Questions.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. xls_qs : str (Path to Excel-Questions file).
        ========================================================================
        """
        self.excel = Excel(xls_qs)
        self.__load_qs()
        self.excel.close()

    def __load_qs(self):
        """
        ========================================================================
         Description: Load Questions from Excel into Dictionary of
                        {int (Qid) -> Quest}
        ========================================================================
        """
        row = self.fr
        while True:
            qid = self.__get_qid(row)
            # Break on EOF
            if not qid:
                break
            is_valid = self.__get_is_valid(row)
            # Continue on invalid Question
            if not is_valid:
                row += 1
                continue
            priority = self.__get_priority(row)
            topics = self.__get_topics(row)
            question = self.__get_question(row)
            ans_true = self.__get_ans_true(row)
            ans_false = self.__get_ans_false(row)
            self.qs[qid] = Quest(qid, priority, topics, question, ans_true,
                                 ans_false)
            row += 1

    def __get_qid(self, row):
        """
        ========================================================================
         Description: Get Qid (Question-Id) from the Excel Row.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. row : int
        ========================================================================
         Return: int
        ========================================================================
        """
        assert type(row) == int
        assert row >= 1
        qid = self.excel.get_value(row, self.col_qid)
        if qid:
            return int(qid)
        return None

    def __get_is_valid(self, row):
        """
        ========================================================================
         Description: Get if Is-Valid Question from the Excel Row.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. row : int
        ========================================================================
         Return: bool
        ========================================================================
        """
        assert type(row) == int
        assert row >= 1
        return bool(self.excel.get_value(row, self.col_valid))

    def __get_priority(self, row):
        """
        ========================================================================
         Description: Get Priority (A|B|C) of the Question.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. row : int
        ========================================================================
         Return: str (A|B|C)
        ========================================================================
        """
        assert type(row) == int
        assert row >= 1
        return self.excel.get_value(row, self.col_priority)

    def __get_topics(self, row):
        """
        ========================================================================
         Description: Get List of Question-Topics from the Excel Row.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. row : int
        ========================================================================
         Return: list of str
        ========================================================================
        """
        assert type(row) == int
        assert row >= 1
        topics = list()
        for col in range(self.col_topic_first, self.col_topic_last + 1):
            topics.append(str(self.excel.get_value(row, col)))
        return topics

    def __get_question(self, row):
        """
        ========================================================================
         Description: Get Question-Text from the Excel Row.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. row : int
        ========================================================================
         Return: str
        ========================================================================
        """
        assert type(row) == int
        assert row >= 1
        return self.excel.get_value(row, self.col_question)

    def __get_ans_true(self, row):
        """
        ========================================================================
         Description: Get True-Answer from the Excel Row.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. row : int
        ========================================================================
         Return: str
        ========================================================================
        """
        assert type(row) == int
        assert row >= 1
        return str(self.excel.get_value(row, self.col_answer_true))

    def __get_ans_false(self, row):
        """
        ========================================================================
        Description: Get List of False-Answers from the Excel Row.
        ========================================================================
        Arguments:
        ------------------------------------------------------------------------
           1. row : int
        ========================================================================
        Return: list of str
        ========================================================================
        """
        assert type(row) == int
        assert row >= 1
        ans_false = list()
        for col in range(self.col_answer_false_first,
                         self.col_answer_false_last + 1):
            ans = self.excel.get_value(row, col)
            if ans is not None:
                ans_false.append(str(ans))
        return ans_false
