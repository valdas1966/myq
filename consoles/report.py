from f_db.c_sqlite import SQLite
from utils import path_myq


path_db = path_myq.get() + '\\myq.db'


def precision():
    sql = SQLite(path_db)
    query = """
                select
                    substr(tazak, 5, 4) as date,
                    round(cast(sum(answered) as real) / sum(asked), 2) as p
                from
                    logger
                group by
                    substr(tazak, 5, 4)
                order by 1 desc
            """
    print(sql.select(query, verbose=False))
    sql.close()


def asked():
    sql = SQLite(path_db)
    query = """
                select
                    asked,
                    count(*) as cnt
                from
                    stat
                group by
                    asked
                order by 1
            """
    print(sql.select(query, verbose=False))
    sql.close()


precision()
print()
asked()
