from quest import Quest


class QuestMultiAnswer(Quest):
    """
    ============================================================================
     Description: Question with Multiple Answer - when the User has to
                    choose the right answer from multiple choices.
    ============================================================================
    """

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
        ans = input(self.text + '-> ')
        if not self.__is_legal_answer(ans):
            return self.ask(counter)
        ans = int(ans)
        # Break
        if ans == 0:
            return False
        # True-Answer (ans-1 because zero-based)
        if self.answers[ans - 1] == self.answer_true:
            return True
        # False-Answer
        self.__print_right_answer()
        return self.ask(counter)

    def __is_legal_answer(self, ans):
        """
        ========================================================================
         Description: Return True if it is Legal-Answer
                        (zero or int in size of the answers-list).
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. ans : str (Answer from the User).
        ========================================================================
         Return: bool
        ========================================================================
        """
        # not int
        if not ans.isnumeric():
            return False
        # Illegal int
        if ans not in [i for i in range(len(self.answers) + 1)]:
            return False
        return True
