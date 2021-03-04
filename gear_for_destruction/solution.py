from fractions import Fraction as frac
def solution(pegs):
    lst = []
    for i in range(len(pegs) - 1):
        lst.append(pegs[i + 1] - pegs[i])

    last_gear = 0
    for i, ele in enumerate(lst):
        if i % 2 == 0:
            last_gear += ele
        else:
            last_gear -= ele

    if len(pegs) % 2 == 0:
        last_gear = frac(last_gear, 3)

    first_gear = frac(last_gear) * 2

    if first_gear <= 0 or last_gear <= 0:
        return [-1, -1]

    ss = [first_gear]
    cur_gear = first_gear
    for element in lst:
        check = element - cur_gear
        if check <= 1:
            return [-1, -1]
        ss.append(check)
        cur_gear = check

    for i in range(len(ss) - 1):
        klo = ss[i] + ss[i + 1]
        if klo != lst[i]:
            return [-1, -1]

    return [first_gear.numerator, first_gear.denominator]