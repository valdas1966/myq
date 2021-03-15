import random
from quest import Quest
from f_utils.c_timer import Timer


class QuestMultiAnswer(Quest):
    """
    ============================================================================
     Description: Question with Multiple Answer - when the User has to
                    choose the right answer from multiple choices.
    ============================================================================
    """

    def __init__(self, qid, row, priority, topic, question,
                 ans_true, ans_false):
        """
        ========================================================================
         Constructor: Init the Private Attributes.
        ========================================================================
        """
        super().__init__(qid, row, priority, topic, question,
                         ans_true, ans_false)
        self.answers = [ans_true]
        if ans_false:
            self.answers.append(ans_false)
        random.shuffle(self.answers)

    def ask(self, counter, repeated=False):
        """
        ========================================================================
         Description: Ask the User a Multi-Answer Question.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. counter : int (Number of the Question in the current Exam).
            2. repeated : bool (Repeated-Question of False-Answer).
        ========================================================================
         Return: bool (True on Legal-Answer, False on Break - End of Exam).
        ========================================================================
        """
        super().ask(counter, repeated)
        # Load Answers
        random.shuffle(self.answers)
        for i, answer in enumerate(self.answers):
            # i+1 because zero-based
            self.text += f'{i + 1}. {answer}\n'
        ans = input(self.text + '-> ')
        # Illegal Answer
        if ans not in {'0', '1', '2'}:
            print('Illegal Answer')
            return self.ask(counter, repeated)
        ans = int(ans)
        # Break
        if ans == 0:
            return False
        # True-Answer (ans-1 because zero-based)
        if self.answers[ans - 1] == self.ans_true:
            if not repeated:
                self._update_stat(answer=True)
            return True
        # False-Answer
        self._print_right_answer()
        if not repeated:
            self._update_stat(answer=False)
        return self.ask(counter, repeated=True)
