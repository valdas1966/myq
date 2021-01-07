from collections import defaultdict
from topic import Topic
from f_excel.c_excel import Excel


class Topics:

    # First Relevant Row in Excel
    fr = 1
    # First Relevant Col in Excel
    fc = 2
    # Level of Topics
    level = defaultdict(list)
    # All Topics
    topics = set()

    def __init__(self, path_myq):
        self.path_myq = path_myq
        li_rows = self.__get_li_rows()
        self.__load(li_rows)

    def __get_li_rows(self):
        """
        ========================================================================
         Description: Return Linked List of Rows and Columns from Excel.
        ========================================================================
         Return: List (Rows) of List (Cols) of Str (Values).
        ========================================================================
        """
        xlsx = self.path_myq + 'topics.xlsx'
        excel = Excel(xlsx)
        li_rows = excel.to_linked_list(self.fr, self.fc)
        excel.close()
        return li_rows

    def __load(self, li_rows):
        """
        ========================================================================
         Description: Fill Class Attributes (Level and Topics).
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. li_rows : List (Rows) of List (Columns) of Str (Values).
        ========================================================================
        """
        for li_cols in li_rows:
            name = ' -> '.join(li_cols[:-1])
            priority = li_cols[-1]
            topic = Topic(name, priority)
            self.level[topic.level].append(topic)
            self.topics.add(topic)

    def __check_valid(self):


t = Topics(path_myq='d:\\myq\\')
print(t.topics)
print(t.level[2])



