from f_utils import u_tester
from quest import Quest


class TestQuest:

    def __init__(self):
        u_tester.print_start(__file__)
        TestQuest.__tester_answers()
        TestQuest.__tester_is_one_answer()
        TestQuest.__tester_index_answer_true()
        TestQuest.__tester_load_stat()
        u_tester.print_finish(__file__)

    @staticmethod
    def __tester_answers():
        quest = Quest(qid=0, priority='A', topics=list(),
                      question='quest test', answer_true='a',
                      answers_false=['b', 'c', None])
        p0 = set(quest.answers) == {'a', 'b', 'c'}
        u_tester.run(p0)

    @staticmethod
    def __tester_is_one_answer():
        quest = Quest(qid=0, priority='B', topics=list(), question='quest test',
                      answer_true='a', answers_false=[None, None, None])
        p0 = quest.is_one_answer
        u_tester.run(p0)

    @staticmethod
    def __tester_index_answer_true():
        quest = Quest(qid=0, priority='C', topics=list(), question='test',
                      answer_true='a', answers_false=['b', 'c'])
        p0 = quest.answers[quest.index_ans_true] == 'a'
        u_tester.run(p0)

    @staticmethod
    def __tester_load_stat():
        quest = Quest(qid=0, priority='A', topics=list(), question='test',
                      answer_true='a', answers_false=['b'])
        quest.load_stat(asked=0, answered=0, last_10=str(),
                        last_time=1000)
        p0 = quest.grade = 100
        u_tester.run(p0)


if __name__ == '__main__':
    TestQuest()
