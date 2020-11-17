import sys
sys.path.append('D:\\mypy')
from f_excel.c_excel import Excel
from q import Q


class QS:
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
    col_id = 1
    col_valid = 2
    col_topic_first = 3
    col_topic_last = 4
    col_question = 5
    col_answer_true = 6
    col_answer_false_first = 7
    col_answer_false_last = 9

    def __init__(self, xls_qs='questions.xlsx'):
        # Dict {int (Id) -> Q (Question)}
        self.qs = dict()
        self.excel = Excel(xls_qs)
        self.__load_qs()
        self.excel.close()

    def __load_qs(self):
        row = self.fr
        while True:
            id = self.excel.get_value(row, self.col_id)
            if not id:
                break
            is_valid = self.excel.get_value(row, self.col_valid)
            if not is_valid:
                row += 1
                continue
            topics = list()
            for col in range(self.col_topic_first, self.col_topic_last + 1):
                topics.append(str(self.excel.get_value(row, col)))
            question = self.excel.get_value(row, self.col_question)
            ans_true = str(self.excel.get_value(row, self.col_answer_true))
            ans_false = list()
            for col in range(self.col_answer_false_first,
                             self.col_answer_false_last+1):
                ans_false.append(str(self.excel.get_value(row, col)))
            q = Q(id, topics, question, ans_true, ans_false)
            self.qs[id] = q
            row += 1


x = QS()
print(len(x.qs))

