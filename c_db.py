from f_db.c_sqlite import SQLite
import utils.path_myq
import pandas as pd


class DB:

    def __init__(self):
        self.path_myq = utils.path_myq.get()
        self.path_db = self.path_myq + '\\myq.db'
        self.sql = SQLite(self.path_db)

    def get_questions(self, id_parent) -> list:
        query = """
                    select
                        qid,
                        
                    """


    def get_id_topic(self, tree: str) -> int:
        """
        ========================================================================
         Description: Get Str-Representation of the Topics-Tree and
                        Return the required Id-Topic.
        ========================================================================
         Arguments:
        ------------------------------------------------------------------------
            1. tree : str (Topics-Tree until the required topic).
        ========================================================================
         Return: int (required Id-Topic).
        ========================================================================
        """
        topics = tree.split('->')
        query = f"select id_topic from topics where topic='{topics[0]}'"
        id_topic = self.sql.select_value(query=query)
        for topic in topics[1:]:
            query = f"""
                        select
                            id_topic
                        from
                            topics
                        where
                            topic='{topic}'
                            and
                            id_parent={id_topic}
                    """
            id_topic = self.sql.select_value(query=query)
        return id_topic

    def insert_topic(self,
                     topic: str,  # Topic-Name
                     tree: str = None,  # Topics-Tree
                     level: int = 0,  # Difficulty-Level
                     priority: str = 'A'  # Topic-Priority by Importance
                     ) -> None:
        """
        ========================================================================
         Description: Insert given by params Topic into the Topics-Table.
        ========================================================================
        """
        tname = 'topics'
        cols = list()
        cols.append('topic')
        cols.append('priority')
        cols.append('level')
        if tree:
            cols.append('id_parent')
        values = list()
        values.append(topic)
        values.append(priority)
        values.append(level)
        if tree:
            values.append(DB.get_id_topic(tree))
        self.sql.insert(tname, values, cols, verbose=True)

    def insert_topics(self) -> None:
        """
        ========================================================================
         Description: Insert Topics from CSV-File into the Topics-Table.
        ========================================================================
        """
        df = pd.read_csv(self.path_myq + '\\topics.csv')
        for _, row in df.iterrows():
            topic = row['topic']
            tree = row['tree']
            level = row['level']
            priority = row['priority']
            self.insert_topic(topic, tree, level, priority)

    def close(self):
        self.sql.commit()
        self.sql.close()
