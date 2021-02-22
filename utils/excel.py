from f_utils import u_file
from f_excel.c_excel import Excel


def get_filepaths_questions():
    dir_questions = '\\'.join(__file__.split('/')[:-2]) + '\\Questions'
    return u_file.filepaths(dir_questions, 'xlsx')


def clear_column(xlsx, i_col):
    assert type(xlsx) == str
    assert type(i_col) == int
    excel = Excel(xlsx)
    excel.ws.max


print(get_filepaths_questions())
