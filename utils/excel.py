from f_utils import u_file
from f_excel.c_excel import Excel


def clear_id_columns():
    """
    ============================================================================
     Description: Clear Id-Columns in all Excel-Questions files.
    ============================================================================
    """
    filepaths = get_filepaths_questions()
    for xlsx in filepaths:
        print(xlsx)
        clear_column(xlsx, col=1, row_start=2)


def get_filepaths_questions():
    """
    ============================================================================
     Description: Return FilePaths of all Excel-Questions Files.
    ============================================================================
     Return: List of Str (Excel-FilePaths).
    ============================================================================
    """
    dir_questions = __file__[0] + ':\\Myq\\Questions'
    return u_file.filepaths(dir_questions, 'xlsx')


def clear_column(xlsx, col, row_start=1):
    """
    ============================================================================
     Description: Clear Column Values in Excel File.
    ============================================================================
     Arguments:
    ----------------------------------------------------------------------------
        1. xlsx : str (Path to Excel-File).
        2. col : int (Index of Column to Clear).
        3. row_start : int (Row to Start Clear from).
    ============================================================================
    """
    assert type(xlsx) == str
    assert type(col) == int
    excel = Excel(xlsx)
    row_last = excel.ws.max_row
    excel.clear_cells(row=row_start, col=col, row_last=row_last)
    excel.close()


# clear_id_columns()
