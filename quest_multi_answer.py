import random
from quest import Quest


class QuestMultiAnswer(Quest):
    """
    ============================================================================
     Description: Question with Multiple Answer - when the User has to
                    choose the right answer from multiple choices.
    ============================================================================
    """

    def __init__(self, qid, priority, topic, question, ans_true, ans_false):
        """
        ========================================================================
         Constructor: Init the Private Attributes.
        ========================================================================
        """
        super().__init__(qid, priority, topic, question, ans_true, ans_false)
        self.answers = [ans_true]
        if ans_false:
            self.answers.append(ans_false)
        random.shuffle(self.answers)

    def ask(self, counter):
        """
        ========================================================================
         Description: Ask the User a Multi-Answer Question.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. counter : int (Number of the Question in the current Exam).
        ========================================================================
         Return: bool (True on Legal-Answer, False on Break - End of Exam).
        ========================================================================
        """
        super().ask(counter)
        # Load Answers
        for i, answer in enumerate(self.answers):
            # i+1 because zero-based
            self.text += f'{i + 1}. {answer}\n'
        ans = input(self.text + '-> ')
        # Illegal Answer
        if ans not in {1, 2}:
            print('illegal')
            return self.ask(counter)
        ans = int(ans)
        # Break
        if ans == 0:
            return False
        # True-Answer (ans-1 because zero-based)
        if self.answers[ans - 1] == self.answer_true:
            return True
        # False-Answer
        self._print_right_answer()
        return self.ask(counter)
