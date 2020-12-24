from collections import defaultdict
from f_excel.c_excel import Excel


class Topics(defaultdict):

    # Row of the First-Topic
    fr = 1
    # Column of the Top-Topic
    fc = 1

    def __init__(self, path_myq):
        super().__init__(defaultdict)
        self.__load(path_myq)

    def __load(self, path_myq):
        xlsx = path_myq + 'topics.xlsx'
        excel = Excel(xlsx)
        row = self.fr
        while not excel.is_blank(row, self.fc):
            col = self.fc
            while not excel.is_blank(row, col):
                name = excel.get_value(row, col)
                priority = excel.get_value(row, col+1)
                if priority in {'A', 'B', 'C'}:
                    self[name] = priority
                col += 1
            row += 1
        excel.close()


t = Topics(path_myq='d:\\myq\\')
print(t)

