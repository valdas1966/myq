from pathlib import Path
from f_db.c_sqlite import Sqlite


path = Path(__file__)
path_myq = f'{str(path.parent)[0]}:\\myq'
path_db = path_myq + '\\myq.db'


def create_table():
    sql = Sqlite(path_db)
    sql.drop(tname='stat')
    command = """
                create table
                    stat
                    (
                        qid int,
                        asked int default 0,
                        answered int default 0,
                        last_10 text default '',
                        last_time int default 100000,
                        priority_val real default 1,
                        grade int default 100
                    )
                """
    sql.run(command)
    sql.close()


# create_table()
