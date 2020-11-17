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

    # Excel Columns
    # Question Id
    col_qid = 1
    # Is Valid Question (1/0)
    col_valid = 2
    # First Topic-Column
    col_topic_first = 3
    # Last Topic-Column
    col_topic_last = 4
    # Text of the Question
    col_question = 5
    # Text of the True-Answer
    col_answer_true = 6
    # First False-Answer Column
    col_answer_false_first = 7
    # Last False-Answer Column
    col_answer_false_last = 9

    # Dict of Questions {int (Qid) -> Quest (Question)}
    qs = dict()

    def __init__(self, xls_qs='questions.xlsx'):
        self.excel = Excel(xls_qs)
        self.__load_qs()
        self.excel.close()

    def __load_qs(self):
        row = self.fr
        while True:
            row += 1
            qid = self.get_qid(row)
            # Break on EOF
            if not qid:
                break
            is_valid = self.__get_is_valid(row)
            # Continue on invalid Question
            if not is_valid:
                continue
            topics = self.__get_topics(row)
            question = self.__get_question(row)
            ans_true = str(self.excel.get_value(row, self.col_answer_true))
            ans_false = list()
            for col in range(self.col_answer_false_first,
                             self.col_answer_false_last+1):
                ans_false.append(str(self.excel.get_value(row, col)))
            self.qs[qid] = Quest(qid, topics, question, ans_true, ans_false)

    def __get_qid(self, row):
        return self.excel.get_value(row, self.col_qid)

    def __get_is_valid(self, row):
        return self.excel.get_value(row, self.col_valid)

    def __get_topics(self, row):
        topics = list()
        for col in range(self.col_topic_first, self.col_topic_last + 1):
            topics.append(str(self.excel.get_value(row, col)))
        return topics

    def __get_question(self, row):
        return self.excel.get_value(row, self.col_question)