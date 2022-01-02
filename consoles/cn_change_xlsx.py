from f_utils import u_file
from f_excel.c_excel import Excel
import re

repo = 'd:\\myq\\questions'
col_q = 4
col_a = 5
fr = 2

for xlsx in u_file.filepaths(repo, extensions='xlsx'):
    excel = Excel(xlsx)
    lr = excel.last_row(fr, col_q)
    for r in range(fr, lr+1):
        q = str(excel.get_value(r, col_q))
        a = str(excel.get_value(r, col_a))
        q_new = re.sub(r'\*{6,}', '*****', q)
        excel.set_value(r, col_q, q_new)
    excel.close()
