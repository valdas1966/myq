from quest import Quest


class QuestYesNo(Quest):
    """
    ============================================================================
     Description: Question with Yes/No Answers - when the User has to choose
                    if the question is True or False.
    ============================================================================
    """

    def ask(self, counter):
        """
        ========================================================================
         Description: Ask the User an Yes-No Answer Question.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. counter : int (Number of the Question in the current Exam).
        ========================================================================
         Return: bool (True on Legal-Answer, False on Break - End of Exam).
        ========================================================================
        """
        super().ask(counter)
        input(text + f'(Yes/No):\n-> ')
        ans = input(self.text + '-> ')
        # True-Answer
        if ans == self.answer_true:
            return True
        # Break
        if ans == '0':
            return False
        # False-Answer
        self.__print_right_answer()
        return self.ask(counter)
