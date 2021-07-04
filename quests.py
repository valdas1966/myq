from f_excel.c_excel import Excel
from f_utils import u_file
from topic import Topic
from f_logger.tazak import LoggerTazak
from f_data_structure.tree import Tree
import factory_quest
from quest_generator import generate


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
    lc = 7

    # ===================
    # Excel Columns
    # ===================
    # Question Id
    col_qid = 1
    # Is Valid Question (1/0)
    col_valid = 2
    # Priority of the Question (A | B | C)
    col_priority = 3
    # Text of the Question
    col_question = 4
    # Text of the True-Answer
    col_ans_true = 5
    # Text of the False-Answer
    col_ans_false = 6
    # Date Created
    col_date_created = 7

    def __init__(self, path_myq, subtree_topics, stat, logger):
        """
        ========================================================================
         Description: Constructor. Init the Dict of Questions.
        ------------------------------------------------------------------------
            1. qs : dict {str (Qid) -> Quest (Question)}
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. path_myq : str (Path to Myq-Directory).
            2. subtree_topics : Tree (SubTree of Relevant Topics).
            3. stat : dict {qid -> tuple of values}
                                    asked, answered, last_10, last_time
            4. logger : TazakLogger
        ========================================================================
        """
        assert type(path_myq) == str
        assert type(subtree_topics) == Tree
        assert type(stat) == dict
        assert type(logger) == LoggerTazak
        # Dict of Questions {str (Qid) -> Quest (Question)}
        self.qs = dict()
        # Set of All Priorities
        self.priorities = set()
        self.path_myq = path_myq
        self.logger = logger
        path_dir = self.path_myq + '\\Questions'
        filepaths = u_file.filepaths(path_dir, extensions='xlsx')
        for xlsx_qs in filepaths:
            name_topic = self.__to_topic_name(xlsx_qs)
            topic = None
            if name_topic in subtree_topics.nodes:
                topic = subtree_topics.nodes[name_topic].data
            self.__load_qs(xlsx_qs, topic)
        self.__load_stat(stat)

    def __to_topic_name(self, xlsx_qs):
        """
        ========================================================================
         Description: Return Topic-Name by Excel-File-Name.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. xlsx_qs : str (Path to Excel-Questions File).
        ========================================================================
         Return: str (Topic Name).
        ========================================================================
        """
        name = xlsx_qs[:-5]
        name = name.replace(f'{self.path_myq}\\Questions\\', '')
        return name.replace('\\', ' -> ')

    def __load_qs(self, xlsx_qs, topic):
        """
        ========================================================================
         Description: Load Questions from Excel into Dictionary of
                        {str (Qid) -> Quest (Question}
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. xlsx_qs : str (Path to Excel-Question File)
            2. topic : Topic Class (of the Excel-Question File).
        ========================================================================
        """
        assert type(xlsx_qs) == str
        excel = Excel(xlsx_qs)
        row = self.fr
        while True:
            qid = self.__get_qid(excel, row)
            # Break on EOF
            if not qid:
                break
            is_valid = self.__get_is_valid(excel, row)
            # Continue on invalid Question
            if not is_valid:
                row += 1
                continue
            priority = '0'
            if topic:
                priority = topic.priority + self.__get_priority(excel, row)
            question = self.__get_question(excel, row)
            ans_true = self.__get_ans_true(excel, row)
            ans_false = self.__get_ans_false(excel, row)
            if self.__need_generation(question):
                question, ans_true, ans_false = generate(question)
            qtype = self.__get_qtype(ans_true, ans_false)
            self.qs[qid] = factory_quest.build(qtype, qid, row, priority, topic,
                                               question, ans_true, ans_false,
                                               self.logger)
            self.priorities.add(priority)
            row += 1
        excel.close()

    @staticmethod
    def __need_generation(question):
        """
        ========================================================================
         Description: Return True if the Question need Generation.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. question : str (Question Text).
        ========================================================================
         Return: bool
        ========================================================================
        """
        assert type(question) == str
        if not question.startswith('Generate #'):
            return False
        elements = question.split(' ')
        try:
            int(elements[1][1:])
        except Exception:
            return False
        return True

    def __load_stat(self, stat):
        """
        ========================================================================
         Description: Load Stat to Questions.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. stat : Dict of Tuple (Stat-Values).
        ========================================================================
        """
        li = sorted(list(self.priorities), reverse=True)
        d = {p: round((i+1) / len(li), 2) for i, p in enumerate(li)}
        for qid, q in self.qs.items():
            asked, answered, last_10, last_time = 0, 0, str(), 1000
            priority_val = d[q.priority]
            if qid in stat:
                vals = stat[qid]
                asked = int(vals[0])
                answered = int(vals[1])
                last_10 = vals[2]
                last_time = int(vals[3])
            q.load_stat(asked, answered, last_10, last_time, priority_val)

    def __get_qid(self, excel, row):
        """
        ========================================================================
         Description: Get Qid (Question-Id) from the Excel Row.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. excel : Excel Class
            2. row : int
        ========================================================================
         Return: int
        ========================================================================
        """
        assert type(excel) == Excel
        assert type(row) == int
        assert row >= 1
        qid = excel.get_value(row, self.col_qid)
        if qid:
            qid = int(qid)
        return qid

    def __get_is_valid(self, excel, row):
        """
        ========================================================================
         Description: Get if Is-Valid Question from the Excel Row.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. excel : Excel Class
            2. row : int
        ========================================================================
         Return: bool
        ========================================================================
        """
        assert type(row) == int
        assert type(excel) == Excel
        assert row >= 1
        return bool(excel.get_value(row, self.col_valid))

    def __get_priority(self, excel, row):
        """
        ========================================================================
         Description: Get Priority (A|B|C) of the Question.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. excel : Excel Class
            1. row : int
        ========================================================================
         Return: str (A|B|C)
        ========================================================================
        """
        assert type(row) == int
        assert type(excel) == Excel
        assert row >= 1
        return excel.get_value(row, self.col_priority)

    def __get_question(self, excel, row):
        """
        ========================================================================
         Description: Get Question-Text from the Excel Row.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. excel : Excel
            1. row : int
        ========================================================================
         Return: str
        ========================================================================
        """
        assert type(row) == int
        assert type(excel) == Excel
        assert row >= 1
        question = excel.get_value(row, self.col_question)
        return question.replace('\\n', '\n')

    def __get_ans_true(self, excel, row):
        """
        ========================================================================
         Description: Get True-Answer from the Excel Row.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. excel : Excel Class
            2. row : int
        ========================================================================
         Return: str
        ========================================================================
        """
        assert type(row) == int
        assert type(excel) == Excel
        assert row >= 1
        return str(excel.get_value(row, self.col_ans_true))

    def __get_ans_false(self, excel, row):
        """
        ========================================================================
        Description: Get List of False-Answers from the Excel Row.
        ========================================================================
        Arguments:
        ------------------------------------------------------------------------
           1. excel : Excel Class
           2. row : int
        ========================================================================
        Return: list of str
        ========================================================================
        """
        assert type(row) == int
        assert type(excel) == Excel
        assert row >= 1
        if excel.is_blank(row, self.col_ans_false):
            return str()
        else:
            return str(excel.get_value(row, self.col_ans_false))

    @staticmethod
    def __get_qtype(ans_true, ans_false):
        """
        ========================================================================
         Description: Return Question-Type (ONE | YESNO | MULTI).
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. ans_true : str (True Answer).
            1. ans_false : str (False Answer).
        ========================================================================
         Return: str (ONE | YESNO | MULTI).
        ========================================================================
        """
        assert type(ans_true) == str
        assert type(ans_false) == str
        if not ans_false:
            return 'ONE'
        if {ans_true, ans_false} == {'Yes', 'No'}:
            return 'YESNO'
        if ans_true:
            return 'MULTI'

