from topic import Topic
from f_logger.tazak import LoggerTazak


class Quest:
    """
    ============================================================================
     Description: Represent a Question.
    ============================================================================
    """
    # Question Id
    qid = 0
    # Question Priority-Value [0,1]
    priority_val = 0
    # Question Topic
    topic = None
    # Question String-Representation
    question = str()
    # Question True-Answer
    ans_true = str()
    # Question False-Answer
    ans_false = str()
    # Random List with True and False Answers
    answers = list()
    # Number of Times the Question has asked
    asked = 0
    # Number of Times the Question has answered correctly
    answered = 0
    # Binary Representation of the last-10 Answers to Questions [1 (T) | 0 (F)]
    last_10 = str()
    # Number of Questions asked since the Last Time
    last_time = 1000
    # Grade of the Question based on its Statistics in range [1, 100]
    grade = 0
    # Length of Delimiter Line of Equal-Sign (=)
    len_delimiter_line = 75
    # Full-Text of Questions and the Answers
    text = str()
    # Input from the User (Answer to the Question)
    ans_user = str()

    def __init__(self, qid, row, priority, topic, question,
                 ans_true, ans_false):
        """
        ========================================================================
         Description: Constructor - Init Attributes.
        ========================================================================
            1. qid : str
            2. row : int (Row in Excel - for Ordering).
            3. priority : str [A | B | C | ABA]
            4. topic : Topic Class
            5. question : str
            6. ans_true : str
            7. ans_false : str
        ========================================================================
        """
        assert type(qid) == str
        assert type(row) == int
        assert type(priority) == str
        assert type(topic) == Topic
        assert type(question) == str
        assert type(ans_true) == str
        assert type(ans_false) == str
        self.qid = qid
        self.row = row
        self.topic = topic
        self.priority = priority
        self.question = question
        self.ans_true = ans_true

    def load_stat(self, asked, answered, last_10, last_time, priority_val):
        """
        ========================================================================
         Description: Load Statistics about the Past of the Question.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. asked : int (Number of Times the Question was asked).
            2. answered : int (Question was answered correctly).
            3. last_10 : str (0 | 1) [Binary representation of last 10 answers).
            4. last_time : int (Number of Questions asked since the last time).
            5. priority_val : float [0,1]
        ========================================================================
        """
        assert type(asked) == int
        assert type(answered) == int
        assert type(last_10) == str
        assert type(last_time) == int
        assert type(priority_val) == float
        self.asked = asked
        self.answered = answered
        self.last_10 = last_10
        self.last_time = last_time
        self.priority_val = priority_val
        self.set_grade()

    def ask(self, counter, repeated=False):
        """
        ========================================================================
         Description: Ask the User a Question.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. counter : int (Number of Question in current Exam).
            3. repeated : bool (Repeated-Question after False-Answer).
        ========================================================================
         Return: bool (True on Legal-Answer, False on Break - End of Exam).
        ========================================================================
        """
        assert type(counter) == int
        assert type(repeated) == bool
        # Load Question
        self.text = f'{"=" * self.len_delimiter_line}\n{self.topic}\n' \
                    f'{"=" * self.len_delimiter_line}\nAsked={self.asked}, ' \
                    f'Answered={self.answered}, Last_10={self.last_10}, ' \
                    f'Last_Time={self.last_time}, '\
                    f'Priority={self.priority_val}, Grade={self.grade}\n' \
                    f'{"=" * self.len_delimiter_line}\n#{counter}. ' \
                    f'{self.question}:\n{"-" * self.len_delimiter_line}\n'

    def set_grade(self):
        """
        ========================================================================
         Description: Return Grade of the Question bases on its Statistics.
        ========================================================================
         Return: int [1, 100]
        ========================================================================
        """
        w_asked = 5
        w_answered = 10
        w_last_10 = 20
        w_last_time = 50
        w_priority = 15
        # Asked - In Range [0, w_asked]
        f_asked = w_asked * min(0, 1 - (self.asked / 1000))
        # Answered - In Range [0, w_answered]
        f_answered = w_answered
        if self.asked:
            f_answered = w_answered * (1 - (self.answered / self.asked))
        # Last 10 - In Range [0, w_last_10]
        f_last_10 = w_last_10
        if self.last_10:
            count_true = self.last_10.count('1')
            f_last_10 = w_last_10 * (1 - (count_true / len(self.last_10)))
        # Last Time - In Range [0, w_last_time]
        f_last_time = w_last_time * min(1, self.last_time / 1000)
        # Priority - In Range [0, w_priority]
        f_priority = w_priority * self.priority_val
        self.grade = max(1, int(f_asked + f_answered + f_last_10 +
                                f_last_time + f_priority))

    def _print_right_answer(self):
        """
        ========================================================================
         Description: Print the Right Answer (on False Answer from the User).
        ========================================================================
        """
        print(f'{"=" * self.len_delimiter_line}\nThe right answer is: '
              f'{self.ans_true}')

    def _update_stat(self, answer):
        """
        ========================================================================
         Description: Update Question-Statistics after True/False Answer.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. answer : bool (True on True-Answer, False on False-Answer).
        ========================================================================
        """
        self.asked += 1
        ch = '0'
        if answer:
            self.answered += 1
            ch = '1'
        self.last_10 = self.last_10[-10:] + ch
        self.last_time = 1
        self.set_grade()


