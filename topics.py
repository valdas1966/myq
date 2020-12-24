from f_excel.c_excel import Excel


class Topics(list):

    # Row of the First-Topic
    fr = 1
    # Column of the Top-Topic
    fc = 1

    def __init__(self, path_myq):
        super().__init__()

    def __load(self, path_myq):
        xlsx = path_myq + 'topics.xlsx'
        excel = Excel(xlsx)
        row = self.fr
        while not excel.is_blank(row, self.fc):
            name = excel.get_value(row, self.fc)
            priority = excel.get_value(row, self.fc+1)


        excel.close()

