from f_utils import u_tester
from topics import Topics
from topic import Topic


class TestTopics:

    def __init__(self):
        u_tester.print_start(__file__)
        TestTopics.__tester_init()
        TestTopics.__tester_get_priorities()
        u_tester.print_finish(__file__)

    @staticmethod
    def __tester_init():
        topics = Topics('g:\\myq\\testers\\')
        p0 = {t.name for t in topics.topics} == {'TA', 'TA -> TB',
                                                 'TA -> TB -> TC', 'TD',
                                                 'TD -> TE'}
        ta = Topic(name='TA', priority='A', i_row=1)
        tb = Topic(name='TA -> TB', priority='A', i_row=1)
        tc = Topic(name='TA -> TB -> TC', priority='A', i_row=1)
        td = Topic(name='TD', priority='A', i_row=1)
        te = Topic(name='TD -> TE', priority='A', i_row=1)
        p1 = topics.level == {0: [ta, td], 1: [tb, te], 2: [tc]}
        p2 = topics.is_valid
        u_tester.run(p0, p1, p2)

    @staticmethod
    def __tester_get_priorities():
        topics = Topics('g:\\myq\\testers\\')
        priorities_test = topics.get_priorities()
        priorities_true = {'BA': 1/5, 'B': 2/5, 'AAB': 3/5, 'AA': 4/5, 'A': 5/5}
        p0 = priorities_test == priorities_true
        u_tester.run(p0)


if __name__ == '__main__':
    TestTopics()
