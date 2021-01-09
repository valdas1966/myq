import os
from collections import defaultdict
from f_excel.c_excel import Excel
from f_utils import u_set
from topic import Topic


class Topics:

    # First Relevant Row in Excel
    fr = 1
    # First Relevant Col in Excel
    fc = 2
    # Level of Topics
    level = defaultdict(list)
    # All Topics
    topics = set()
    # Excel-Topics file is appropriate to Topics in the Folders
    is_valid = None
    # Delimiter in the Topic-Name represents the Topic-Hierarchy
    delimiter = ' -> '

    def __init__(self, path_myq):
        """
        ========================================================================
         Description: Constructor. Init the Class Attributes.
        ------------------------------------------------------------------------
            1. topics : set of Topic (All Topics).
            2. level : dict of list {int (Level) -> list of Topic}.
            3. is_valid : bool (Excel-Topics equals to Question-Files.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. path_myq : str (Path to Myq-Directory).
        ========================================================================
        """
        self.path_myq = path_myq
        li_rows = self.__get_li_rows()
        self.__load(li_rows)
        self.__check_valid()

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
            name = self.delimiter.join(li_cols[:-1])
            priority = li_cols[-1]
            father = self.__get_father(name)
            if father:
                priority = father.priority + priority
            topic = Topic(name, priority)
            self.level[topic.level].append(topic)
            self.topics.add(topic)

    def __get_father(self, name):
        """
        ========================================================================
         Description: Return Father (Topic) of a given Topic-Name.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. name : str (Topic-Name).
        ========================================================================
         Return: Topic (Father of the given Topic-Name).
        ========================================================================
        """
        name_father = self.delimiter.join(name.split(self.delimiter)[:-1])
        for t in self.topics:
            if t.name == name_father:
                return t

    def __check_valid(self):
        """
        ========================================================================
         Description: Set Private Attribute Is_Valid to True if Excel-Topics
                        file is appropriate to Topics in the Folders.
        ========================================================================
         Return: bool
        ========================================================================
        """
        dir_questions = f'{self.path_myq}\\Questions'
        set_topics = set()
        for root, dirs, files in os.walk(dir_questions):
            for d in dirs:
                set_topics.add(os.path.join(root, d))
            for f in files:
                set_topics.add(os.path.join(root, f))
        set_topics = {t.replace(f'{dir_questions}\\', '') for t in set_topics}
        set_topics = {t.replace('.xlsx', '') for t in set_topics}
        set_topics = {t.replace('\\', ' -> ') for t in set_topics}
        set_topics_xlsx = {t.name for t in self.topics}
        self.is_valid = set_topics == set_topics_xlsx
        if not self.is_valid:
            print(set_topics - set_topics_xlsx)
            print(set_topics_xlsx - set_topics)
