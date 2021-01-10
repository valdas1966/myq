import random
from topic import Topic


class Quest:
    """
    ============================================================================
     Description: Represent a Question.
    ============================================================================
    """
    # Question Id
    qid = 0
    # Question Priority (A | B | C)
    priority = 'A'
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

    def __init__(self, qid, priority, topic, question, ans_true, ans_false):
        """
        ========================================================================
         Description: Constructor - Init Attributes.
        ========================================================================
            1. qid : str
            2. priority : str (A | B | C | ABC | ABBA)
            3. topic : Topic Class
            4. question : str
            5. ans_true : str
            6. ans_false : str
        ========================================================================
        """
        assert type(qid) == str
        assert type(priority) == str
        assert type(topic) == Topic
        assert type(question) == str
        assert type(ans_true) == str
        assert type(ans_false) == str
        self.qid = qid
        self.topic = topic
        self.priority = priority
        self.question = question
        self.ans_true = ans_true

    def load_stat(self, asked, answered, last_10, last_time):
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
        ========================================================================
        """
        assert type(asked) == int
        assert type(answered) == int
        assert type(last_10) == str
        assert type(last_time) == int
        self.asked = asked
        self.answered = answered
        self.last_10 = last_10
        self.last_time = last_time
        self.grade = self.__set_grade()

    def ask(self, counter):
        """
        ========================================================================
         Description: Ask the User a Question.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. counter : int (Number of Question in current Exam).
        ========================================================================
         Return: bool (True on Legal-Answer, False on Break - End of Exam).
        ========================================================================
        """
        # Load Question
        self.text = f'{"=" * self.len_delimiter_line}\n#{counter}. ' \
                    f'{self.question}:\n{"-" * self.len_delimiter_line}\n'

    def _print_right_answer(self):
        """
        ========================================================================
         Description: Print the Right Answer (on False Answer from the User).
        ========================================================================
        """
        print(f'{"=" * self.len_delimiter_line}\nThe right answer is: '
              f'{self.ans_true}')

    def __set_grade(self):
        """
        ========================================================================
         Description: Return Grade of the Question bases on its Statistics.
        ========================================================================
         Return: int [1, 100]
        ========================================================================
        """
        f_asked = 10 * min(1, 1 - (self.asked / 1000))
        f_answered = 20
        if self.asked:
            f_answered = 20 * (1 - (self.answered / self.asked))
        f_last_10 = 40
        if self.last_10:
            count_true = self.last_10.count('1')
            f_last_10 = 40 * (1 - (count_true / len(self.last_10)))
        f_last_time = 10 * min(1, self.last_time / 1000)
        f_priority = 0
        if self.priority == 'A':
            f_priority = 20
        elif self.priority == 'B':
            f_priority = 10
        return max(1, int(f_asked + f_answered + f_last_10 + f_last_time +
                          f_priority))
