from f_db.c_sqlite import Sqlite
import pandas as pd


class DB:

    def __init__(self, path_myq):
        path_db = path_myq + '\\myq.db'
        self.sql = Sqlite(path_db)

    def get_stat(self):
        """
        ========================================================================
         Description: Return Dict of Stat-Data.
        ========================================================================
         Return: dict {int: Series} (qid -> Series of Stat-Data).
        ========================================================================
        """
        dict_stat = dict()
        df = self.sql.select('stat')
        for i_row, values in df.iterrows():
            qid = values['qid']
            dict_stat[qid] = values.drop('qid')
        return dict_stat

    def init_stat(self, qids):
        df = pd.DataFrame({'qid': qids})
        # Delete invalid Questions
        self.sql.load(df=df, tname='qids_relevant', verbose=False)
        command = """
                    delete from
                        stat
                    where
                        qid not in
                        (
                            select
                                qid
                            from
                                qids_relevant
                        )
                  """
        # Insert New Questions
        self.sql.run(command, verbose=False)
        command = """
                    insert into
                        stat(qid)
                    select
                        t1.qid
                    from
                        qids_relevant t1
                    left join
                        stat t2
                    on
                        t1.qid = t2.qid
                    where
                        t2.qid is null
                  """
        self.sql.run(command, verbose=False)

    def close(self):
        self.sql.close()
