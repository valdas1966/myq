from random import randint
from f_math.numbers import u_factors
from f_math.numbers import u_multiples


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
    ans_true = str(n1 + n2)
    ans_false = str()
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
    ans_true = str(n1 - n2)
    ans_false = str()
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
    ans_true = str(n1 * n2)
    ans_false = str()
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
    ans_true = str(n1)
    ans_false = str()
    return question, ans_true, ans_false


def __generate_5():
    """
    ============================================================================
     Description: Square Operation of Middle Natural Numbers.
    ============================================================================
    """
    n = randint(0, 50)
    question = f'{n}^2 = ?'
    ans_true = str(n * n)
    ans_false = str()
    return question, ans_true, ans_false


def __generate_6():
    """
    ============================================================================
     Description: Square Operation of Middle Natural Numbers.
    ============================================================================
    """
    n = randint(0, 50)
    question = f'Sqrt({n * n}) = ?'
    ans_true = str(n)
    ans_false = str()
    return question, ans_true, ans_false


def __generate_7():
    """
    ============================================================================
     Description: Factors of Integer.
    ============================================================================
    """
    n = randint(1, 100)
    factors = u_factors.factors(n)
    question = f'factors({n}) = ?'
    ans_true = ','.join(sorted([str(x) for x in factors]))
    ans_false = str()
    return question, ans_true, ans_false


def __generate_8():
    """
    ============================================================================
     Description: Common Factors of two Integers.
    ============================================================================
    """
    a = randint(1, 100)
    b = randint(1, 100)
    common = u_factors.common_factors(a, b)
    question = f'common_factors({a},{b}) = ?'
    ans_true = ','.join(sorted([str(x) for x in common]))
    ans_false = str()
    return question, ans_true, ans_false


def __generate_9():
    """
    ============================================================================
     Description: Greatest Common Factors of two Integers.
    ============================================================================
    """
    a = randint(1, 100)
    b = randint(1, 100)
    gcf = u_factors.gcf(a, b)
    question = f'gcf({a},{b}) = ?'
    ans_true = str(gcf)
    ans_false = str()
    return question, ans_true, ans_false


def __generate_10():
    """
    ============================================================================
     Description: Least Common Multiples of two given numbers.
    ============================================================================
    """
    a = randint(1, 20)
    b = randint(1, 20)
    lcm = u_multiples.lcm(a, b)
    question = f'lcm({a},{b}) = ?'
    ans_true = str(lcm)
    ans_false = str()
    return question, ans_true, ans_false
