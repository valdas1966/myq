from f_utils import u_file
from f_excel.c_excel import Excel

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
        size = 25
        if ' ' in a:
            continue
        if '*'*size not in q:
            continue
        i = q.find('*' * size)
        if i+size < len(q):
            if 'a' <= q[i+size] <= 'z':
                continue
        sub = q[max(0,i-1):i+size]
        print(len(a)-int(sub[0] != ' '), )
        sub_new = sub[0] + '*'*(len(a)-int(sub[0] != ' '))
        print(q)
        q = q.replace(sub, sub_new)
        print(q)
        excel.set_value(r, col_q, q)
    excel.close()
