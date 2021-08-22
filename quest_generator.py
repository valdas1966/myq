from random import randint
from f_math.number import u_digit
from f_math.number import u_factor
from f_math.number import u_multiple


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
    factors = u_factor.factors(n)
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
    common = u_factor.common_factors(a, b)
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
    gcf = u_factor.gcf(a, b)
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
    lcm = u_multiple.lcm(a, b)
    question = f'lcm({a},{b}) = ?'
    ans_true = str(lcm)
    ans_false = str()
    return question, ans_true, ans_false


def __generate_11():
    """
    ============================================================================
     Description: Sum of two given digits.
    ============================================================================
    """
    a, b = (randint(0, 9) for _ in range(2))
    prev = randint(0, 1)
    remainder, whole = u_digit.plus(a, b, prev)
    question = f'f_math.u_digit.plus(a={a}, b={b}, prev={prev}) -> remainder, ' \
               f'whole -> *****,*****'
    ans_true = f'{remainder},{whole}'
    ans_false = str()
    return question, ans_true, ans_false


def __generate_12():
    """
    ============================================================================
     Description: Multiplication of two given digits.
    ============================================================================
    """
    a, b = (randint(0, 9) for _ in range(2))
    prev = randint(0, 8)
    remainder, whole = u_digit.mult(a, b, prev)
    question = f'f_math.u_digit.mult(a={a}, b={b}, prev={prev}) -> ' \
               'remainder, whole -> *****,*****'
    ans_true = f'{remainder},{whole}'
    ans_false = str()
    return question, ans_true, ans_false


def __generate_13():
    """
    ============================================================================
     Description: a // b
    ============================================================================
    """
    a = randint(0, 9)
    b = randint(1, 9)
    question = f'{a} // {b} = ?'
    ans_true = str(a // b)
    ans_false = str()
    return question, ans_true, ans_false


def __generate_14():
    """
    ============================================================================
     Description: a % b
    ============================================================================
    """
    a = randint(0, 9)
    b = randint(1, 9)
    question = f'{a} % {b} = ?'
    ans_true = str(a % b)
    ans_false = str()
    return question, ans_true, ans_false


def __generate_15():
    """
    ============================================================================
     Description: Power(a, b)
    ============================================================================
    """
    a = randint(0, 10)
    b = randint(0, 3)
    question = f'{a}**{b} = ?'
    ans_true = str(a**b)
    ans_false = str()
    return question, ans_true, ans_false
