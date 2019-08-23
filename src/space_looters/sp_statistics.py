from itertools import product, combinations_with_replacement
from collections import Counter
from fractions import Fraction

def damage(dices):
    kind_list = ["B", "D", "P"]
    sum_maxi = {}
    sum_mean = {}
    sum_var = {}

    for kind in kind_list:
        sum_maxi[kind] = 0
        sum_mean[kind] = 0
        sum_var[kind] = 0
        for die in dices:
            maxi = max(int(face[1]) for face in die if len(face) > 1 and face[0] == kind)
            mean = sum(int(face[1]) for face in die if len(face) > 1 and face[0] == kind)/len(die)
            var = sum((int(face[1])-mean)**2 for face in die if len(face) > 1 and face[0] == kind)/len(die)

            sum_maxi[kind] += maxi
            sum_mean[kind] += mean
            sum_var[kind] += var

    return (sum_maxi, sum_mean, sum_var)

def proba_for(to_get, dices):
    to_get = Counter(to_get)
    pos = list(product(*dices))
    ok = [x for x in pos if len(to_get-Counter(x)) == 0]
    return Fraction(len(ok), len(pos))

def run():
    m_dice = ["M", "M", "M", "C", "E", "R"]
    c_dice = ["C", "C", "C", "E", "M", "S"]
    e_dice = ["E", "E", "E", "M", "C", "T"]

    j_dice = ["B1", "B1", "B1", "D1", "P1", "P1"]
    o_dice = ["B3", "B2", "D2", "D1", "P2", "P2"]
    r_dice = ["B5", "D4", "D3", "J", "P3", "P3"]

    p = proba_for(["M", "M"], [m_dice, m_dice, m_dice])

    print(p, float(p), 1/float(p))
    print(damage([j_dice, j_dice, j_dice, r_dice]))
