from random import randint


def generate(question):
    """
    ============================================================================
     Description: Generate Question by Scenario.
    ============================================================================
     Arguments:
    ----------------------------------------------------------------------------
        1. question : str (in format of: 'Generate 1')
    ============================================================================
     Return: Tuple(str, str, str) (question, ans_true, ans_false)
    ============================================================================
    """
    id = question.split(' ')[1][1:]
    func = f'__generate_{id}'
    return globals()[func]()


def __generate_1():
    """
    ============================================================================
     Description: Sum Operation of Middle Natural Numbers.
    ============================================================================
    """
    n1 = randint(10, 999)
    n2 = randint(10, 999)
    question = f'{n1} + {n2} = ?'
    ans_true = n1 + n2
    ans_false = None
    return question, ans_true, ans_false


def __generate_2():
    """
    ============================================================================
     Description: Minus Operation of Middle Natural Numbers.
    ============================================================================
    """
    n1 = randint(10, 999)
    n2 = randint(10, 999)
    question = f'{n1} - {n2} = ?'
    ans_true = n1 - n2
    ans_false = None
    return question, ans_true, ans_false


def __generate_3():
    """
    ============================================================================
     Description: Multiplication Operation of Middle Natural Numbers.
    ============================================================================
    """
    n1 = randint(0, 100)
    n2 = randint(0, 100)
    question = f'{n1} * {n2} = ?'
    ans_true = n1 * n2
    ans_false = None
    return question, ans_true, ans_false


def __generate_4():
    """
    ============================================================================
     Description: Division Operation of Middle Natural Numbers.
    ============================================================================
    """
    n1 = randint(1, 100)
    n2 = randint(1, 100)
    mult = n1 * n2
    question = f'{mult} / {n2} = ?'
    ans_true = n1
    ans_false = None
    return question, ans_true, ans_false


def __generate_5():
    """
    ============================================================================
     Description: Square Operation of Middle Natural Numbers.
    ============================================================================
    """
    n = randint(0, 50)
    question = f'{n}^2 = ?'
    ans_true = n * n
    ans_false = None
    return question, ans_true, ans_false


def __generate_6():
    """
    ============================================================================
     Description: Square Operation of Middle Natural Numbers.
    ============================================================================
    """
    n = randint(0, 50)
    question = f'Sqrt({n * n}) = ?'
    ans_true = n
    ans_false = None
    return question, ans_true, ans_false
