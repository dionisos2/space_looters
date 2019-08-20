from itertools import product, combinations_with_replacement
from collections import Counter
from fractions import Fraction


def proba_for(to_get, dices):
    to_get = Counter(to_get)
    pos = list(product(*dices))
    ok = [x for x in pos if len(to_get-Counter(x)) == 0]
    return Fraction(len(ok), len(pos))

def run():
    m_dice = ["M", "M", "M", "C", "E", "R"]
    c_dice = ["C", "C", "C", "E", "M", "S"]
    e_dice = ["E", "E", "E", "M", "C", "T"]

    p = proba_for(["M", "M"], [m_dice, m_dice, m_dice])

    print(p, float(p), 1/float(p))
