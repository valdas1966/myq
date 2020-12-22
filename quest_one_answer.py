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

    def ask(self, counter):
        """
        ========================================================================
         Description: Ask the User an One-Answer Question.
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
        # True-Answer
        if ans == self.answer_true:
            return True
        # Break
        if ans == '0':
            return False
        # False-Answer
        self.__print_right_answer()
        return self.ask(counter)
