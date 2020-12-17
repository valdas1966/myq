import random


class Quest:
    """
    ============================================================================
     Description: Represent a Question.
    ============================================================================
    """
    # Question Id
    qid = 0
    # Question Type (SIMPLE | ONE | YESNO)
    qtype = None
    # Question Priority (A | B | C)
    priority = 'A'
    # Question Topics (Main | Sub)
    topics = list()
    # Question String-Representation
    question = str()
    # Question True-Answer
    answer_true = str()
    # List of Question False-Answers
    answers_false = list()
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

    def __init__(self, qid, qtype, priority, topics, question,
                 answer_true, answers_false):
        """
        ========================================================================
         Description: Constructor - Init Attributes.
        ========================================================================
            1. qid : int
            2. qtype : str (SIMPLE | ONE | YESNO)
            2. priority : str (A | B | C)
            3. topics : list of str
            4. question : str
            5. ans_true : str
            6. ans_false : list of str
        ========================================================================
        """
        assert type(qid) == int
        assert type(qtype) == str
        assert type(priority) == str
        assert type(topics) == list
        assert type(question) == str
        assert type(answer_true) == str
        assert type(answers_false) == list
        self.qid = qid
        self.qtype = qtype
        self.topics = topics
        self.priority = priority
        self.question = question
        self.answer_true = answer_true
        # Drop Null False-Answers (Excel Questions may have Nulls False-Answers)
        self.answers_false = list(filter(None, answers_false))
        self.answers = self.answers_false + [self.answer_true]
        self.shuffle_answers()

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
        text = f'{"=" * self.len_delimiter_line}\n#{counter}. ' \
               f'{self.question}:\n{"-" * self.len_delimiter_line}\n'
        if self.qtype == 'ONE':
            return self.__ask_one_answer_question(text)
        if self.qtype == 'YESNO':
            return self.__ask_yes_no_answer_question(text)
        return self.__ask_multi_answer_question(text)

    def __ask_one_answer_question(self, text):
        ans = input(text + '-> ')
        # True-Answer
        if ans == self.answer_true:
            return True
        # Break
        if ans == '0':
            return False
        # False-Answer
        print(f'{"=" * self.len_delimiter_line}\nThe right answer is: '
              f'{self.answer_true}')
        return self.__ask_one_answer_question(text)

    def __ask_yes_no_answer_question(self, text):
        ans = input(text + f'(Yes/No):\n-> ')
        # Break
        if ans == '0':
            return False
        if ans in {'1', 'y', 'Y', 'Yes', 'YES', 'yes'}:
            ans = 'Yes'
        elif ans in {'2', 'n', 'N', 'No', 'NO', 'no'}:
            ans = 'No'
        # Illegal-Answer
        if ans not in {'Yes', 'No'}:
            return self.ask_yes_no_answer_question(text)
        # True-Answer
        if ans == self.answer_true:
            return True
        # False-Answer
        print(f'{"=" * self.len_delimiter_line}\nThe right answer is: '
              f'{self.answer_true}')
        return self.__ask_yes_no_answer_question(text)

    def __ask_multi_answer_question(self, text):
        text_temp = text
        for i, answer in enumerate(self.answers):
            # i+1 because zero-based
            text_temp += f'{i + 1}. {answer}\n'
        ans = input(text_temp + '-> ')
        if ans.isnumeric():
            ans = int(ans)
        else:
            ans = -1
        # Break
        if ans == 0:
            return False
        # Illegal-Answer
        if ans not in [i for i in range(len(self.answers) + 1)]:
            return self.__ask_multi_answer_question(text)
        # True-Answer (ans-1 because zero-based)
        if self.answers[ans - 1] == self.answer_true:
            return True
        # False-Answer
        # ans-1 because zero-based
        print(f'{"=" * self.len_delimiter_line}\nThe right answer is: '
              f'{self.answer_true}')
        random.shuffle(self.answers)
        return self.__ask_multi_answer_question(text)

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
