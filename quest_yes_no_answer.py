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
        text = f'{self.text}(Yes/No):\n-> '
        ans = input(text)
        # Break
        if ans == '0':
            return False
        if ans in {'1', 'Yes', 'YES', 'yes', 'Y', 'y'}:
            ans = 'Yes'
        elif ans in {'2', 'No', 'NO', 'no', 'N', 'n'}:
            ans = 'No'
        # Illegal Answer
        else:
            return self.ask(counter)
        # True-Answer
        if ans == self.ans_true:
            return True
        # False-Answer
        self._print_right_answer()
        return self.ask(counter)
