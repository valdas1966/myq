from f_utils import u_tester
from topic import Topic


class TestTopic:

    def __init__(self):
        u_tester.print_start(__file__)
        TestTopic.__tester_init()
        u_tester.print_finish(__file__)

    @staticmethod
    def __tester_init():
        t = Topic(name='A -> B -> C', priority='ABA', i_row=8)
        p0 = t.name == 'A -> B -> C'
        p1 = t.priority == 'ABA'
        p2 = t.i_row == 8
        p3 = t.level == 2
        u_tester.run(p0, p1, p2, p3)


if __name__ == '__main__':
    TestTopic()
