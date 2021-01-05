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
        li_rows = self.__get_li_rows(path_myq)
        self.__load(li_rows)

    def __get_li_rows(self, path_myq):
        xlsx = path_myq + 'topics.xlsx'
        excel = Excel(xlsx)
        li_rows = excel.to_linked_list(self.fr, self.fc)
        excel.close()
        return li_rows

    def __load(self, li_rows):
        for li_cols in li_rows:
            name = ' -> '.join(li_cols[:-1])
            priority = li_cols[-1]
            topic = Topic(name, priority)
            self.level[topic.level].append(topic)
            self.topics.add(topic)


t = Topics(path_myq='d:\\myq\\')
print(t.topics)
print(t.level[2])



