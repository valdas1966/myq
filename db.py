from f_db.c_sqlite import SQLite
import utils.path_myq


class DB:

    def __init__(self):
        self.path_myq = utils.path_myq.get()
        self.path_db = self.path_myq + '\\myq.db'
        self.sql = SQLite(self.path_db)

    def _get_max_qid(self):
        """
        ========================================================================
         Description: Return Max-Qid-Value in the Stat-Table.
        ========================================================================
         Return: int (Max-Qid-Value)
        ========================================================================
        """
        query = 'select max(qid) as qid_max from stat'
        return int(self.sql.select_first_value(query))
        
    def _get_stat(self):
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

    def _update_stat(self, df_stat):
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
        
    def _update_logger(self, df_logger):
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

    @classmethod
    def get_max_qid(cls):
        """
        ========================================================================
         Description: Return Max-Qid-Value in the Stat-Table.
        ========================================================================
         Return: int (Max-Qid-Value)
        ========================================================================
        """
        db = DB()
        max_qid = db._get_max_qid()
        db.close()
        return max_qid

    @classmethod
    def get_stat(cls):
        """
        ========================================================================
         Description: Return Dict of Stat-Data.
        ========================================================================
         Return: dict {int: Series} (qid -> Series of Stat-Data).
        ========================================================================
        """
        db = DB()
        stat = db._get_stat()
        db.close()
        return stat

    @classmethod
    def update(cls, df_stat, df_logger):
        """
        ========================================================================
         Description: Update Stat and Logger tables.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. df_stat : DataFrame
            2. df_logger : DataFrame
        ========================================================================
        """
        db = DB()
        db._update_stat(df_stat)
        db._update_logger(df_logger)
        db.close()