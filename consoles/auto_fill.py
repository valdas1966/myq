from datetime import datetime
import params
from utils import excel as u_excel
from f_excel.c_excel import Excel
from f_utils import u_datetime


def fill_id():
    """
    ============================================================================
     Description: Auto-Fill Id-Column with Incremental Integer.
    ============================================================================
    """
    col_id = 1
    row_first = 2
    id_last = params.get('id last')
    filepaths = u_excel.get_filepaths_questions()
    for xlsx in filepaths:
        excel = Excel(xlsx)
        row_last = excel.ws.max_row
        for row in range(row_first, row_last+1):
            if excel.is_blank(row, col_id):
                excel.set_value(row, col_id, id_last+1)
                id_last += 1
        excel.close()
    params.set('id last', id_last)
        

def fill_valid():
    """
    ============================================================================
     Description: Auto-Fill Valid-Column with 1 Values (Is Valid).
    ============================================================================
    """
    col_valid = 2
    row_first = 2
    filepaths = u_excel.get_filepaths_questions()
    for xlsx in filepaths:
        excel = Excel(xlsx)
        row_last = excel.ws.max_row
        for row in range(row_first, row_last+1):
            if excel.is_blank(row, col_valid):
                excel.set_value(row, col_valid, 1)
        excel.close()


def fill_priority():
    """
    ============================================================================
     Description: Auto-Fill Priority-Column with 'A' Value.
    ============================================================================
    """
    col_priority = 1
    row_first = 2
    filepaths = u_excel.get_filepaths_questions()
    for xlsx in filepaths:
        excel = Excel(xlsx)
        row_last = excel.ws.max_row
        for row in range(row_first, row_last + 1):
            if excel.is_blank(row, col_priority):
                excel.set_value(row, col_priority, 'A')
        excel.close()


def fill_date():
    """
    ============================================================================
     Description: Auto-Fill Priority-Column with 'A' Value.
    ============================================================================
    """
    col_date = 7
    row_first = 2
    date = u_datetime.to_str(datetime.now(), 'yymmdd')
    filepaths = u_excel.get_filepaths_questions()
    for xlsx in filepaths:
        excel = Excel(xlsx)
        row_last = excel.ws.max_row
        for row in range(row_first, row_last + 1):
            if excel.is_blank(row, col_date):
                excel.set_value(row, col_date, date)
        excel.close()


fill_id()
fill_valid()
fill_priority()
fill_date()
