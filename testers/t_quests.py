from f_utils import u_tester
from quests import Quests


class TestQuests:

    def __init__(self):
        u_tester.print_start(__file__)
        TestQuests.__tester_init()
        u_tester.print_finish(__file__)

    @staticmethod
    def __tester_init():
        xls_qs = 'test.xlsx'
        quests = Quests(xls_qs)
        p0 = len(quests.qs) == 2
        p1 = quests.qs[1].priority = 'A'
        p2 = quests.qs[1].topics = ['Topic1', 'Topic2']
        p3 = quests.qs[1].question = 'Quest1'
        p4 = quests.qs[1].answer_true = 'Ans1'
        p5 = quests.qs[3].answer_true = '2'
        p6 = set(quests.qs[3].answers) == {'2', '3'}
        p7 = quests.qs[1].qtype = 'ONE'
        u_tester.run(p0, p1, p2, p3, p4, p5, p6, p7)


if __name__ == '__main__':
    TestQuests()

