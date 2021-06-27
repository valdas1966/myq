import os
from f_excel.c_excel import Excel


class Exam:
    
    def __init__(self, path_myq):
        self.path_myq = path_myq
        ordered_topics = self.__from_excel()
        
    def __from_excel(self):
        """
        ========================================================================
         Description: Extract Data from Excel into Ordered List.
        ========================================================================
         Return: List of Tuple(str, int) (Topic, Size).
        ======================================================================== 
        """
        fr = 2
        col_size = 2
        col_topic = 3
        ordered_topics = dict()
        xlsx = os.path.join(self.path_myq, 'exam.xlsx')
        excel = Excel(xlsx)
        lr = excel.lr(fr, col_size)
        for r in range(fr, lr+1):
            topic = excel.get_value(r, col_topic)
            size = excel.get_value(r, col_size)
            ordered_topics = (topic, size)
        excel.close()
        return ordered_topics
        