from quest import Quest


class QuestOneAnswer(Quest):
    """
    ============================================================================
     Description: Question with One Answer - when the User is required to type
                    the full answer himself.
    ============================================================================
     Example: What is the acronym of HTML? Answer: Hyper Text Markup Language
    ============================================================================
    """

    def ask(self, counter, repeated=False):
        """
        ========================================================================
         Description: Ask the User an One-Answer Question.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. counter : int (Number of the Question in the current Exam).
            2. repeated : bool (Repeated-Question after False-Answer).
        ========================================================================
         Return: bool (True on Legal-Answer, False on Break - End of Exam).
        ========================================================================
        """
        super().ask(counter, repeated)
        ans = input(self.text + '-> ')
        # True-Answer
        if ans == self.ans_true:
            if not repeated:
                self._update_stat(answer=True)
            return True
        # Break
        if ans == '0':
            return False
        # False-Answer
        self._print_right_answer()
        if not repeated:
            self._update_stat(answer=False)
        return self.ask(counter, repeated=True)
