from c_db import DB


def create_topics():
    cols = list()
    cols.append('id_topic integer primary key autoincrement')
    cols.append('id_parent integer default 0')
    cols.append('valid integer default 1')
    cols.append('topic text not null')
    cols.append('level integer default 0')
    cols.append('priority text default A')
    cols.append('id_topic_old integer default 0')
    cols.append('created datetime default current_timestamp')
    db = DB()
    db.sql.create(tname='topics', cols=cols, verbose=True)
    db.close()


def create_questions():
    cols = list()
    cols.append('qid integer primary key autoincrement')
    cols.append('id_topic integer not null')
    cols.append('valid integer default 1')
    cols.append('question text not null')
    cols.append('answer text not null')
    cols.append('type text default SINGLE')
    cols.append('level integer default 0')
    cols.append('qid_same integer default 0')
    cols.append('qid_old integer default 0')
    cols.append('created datetime current_timestamp')
    db = DB()
    db.sql.create(tname='questions', cols=cols, verbose=True)
    db.close()
