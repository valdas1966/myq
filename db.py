from f_db.c_sqlite import Sqlite
import pandas as pd


class DB:

    def __init__(self, path_myq):
        self.path_db = path_myq + '\\myq.db'
        self.sql = None

    def open(self):
        self.sql = Sqlite(self.path_db)

    def get_stat(self):
        """
        ========================================================================
         Description: Return Dict of Stat-Data.
        ========================================================================
         Return: dict {int: Series} (qid -> Series of Stat-Data).
        ========================================================================
        """
        dict_stat = dict()
        df = self.sql.select('stat', verbose=False)
        for i_row, values in df.iterrows():
            qid = values['qid']
            dict_stat[qid] = values.drop('qid')
        return dict_stat

    def update_stat(self, df_stat):
        """
        ========================================================================
         Description: Update Stat-Table with new statistics values.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. df_stat : DataFrame (with updated statistics values).
        ========================================================================
        """
        self.sql.load(tname='stat', df=df_stat, verbose=False)
        
    def update_logger(self, df_logger):
        """
        ========================================================================
         Description: Insert into Logger-Table new logs.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. df_logger : DataFrame
        ========================================================================
        """
        self.sql.load(tname='temp_logger', df=df_logger, verbose=False)
        self.sql.insert_into(tname_from='temp_logger', tname_to='logger', 
                             verbose=False)

    def close(self):
        self.sql.commit()
        self.sql.close()
