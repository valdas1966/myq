from datetime import datetime
from utils import excel as u_excel
from f_excel.c_excel import Excel
from f_utils import u_datetime
from db import DB


def auto_fill():
    """
    ============================================================================
     Description: AutoFill Excel-Questions Columns (Id, Valid, Priority, Date).
    ============================================================================
    """
    row_first = 2
    col_id = 1
    col_valid = 2
    col_priority = 3
    col_question = 4
    col_date = 7
    date = u_datetime.to_str(datetime.now(), 'yymmdd')
    id_last = DB.get_max_qid()
    filepaths = u_excel.get_filepaths_questions()
    for xlsx in filepaths:
        changed = False
        excel = Excel(xlsx)
        row_last = excel.ws.max_row
        for row in range(row_first, row_last+1):
            if excel.is_blank(row, col_question):
                continue
            # AutoFill Id
            if excel.is_blank(row, col_id):
                excel.set_value(row, col_id, id_last + 1)
                id_last += 1
                changed = True
            # AutoFill Valid
            if excel.is_blank(row, col_valid):
                excel.set_value(row, col_valid, 1)
                changed = True
            # AutoFill Priority
            if excel.is_blank(row, col_priority):
                excel.set_value(row, col_priority, 'A')
                changed = True
            # AutoFill Date
            if excel.is_blank(row, col_date):
                excel.set_value(row, col_date, date)
                changed = True
        excel.close()
        if changed:
            print(xlsx)


auto_fill()
