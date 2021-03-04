def recusive_solution(l):
    if len(l) == 0:
        return 0
    elif len(l) == 1:
        return 1
    else:
        cur_divs = []
        counter = 0
        for e in l:
            for ele in l[e[0] + 1:]:
                if ele[1] % e[1] == 0:
                    cur_divs.append(ele)
            return recusive_solution(cur_divs)

            for div in cur_divs:
                for element in l[div[0] + 1:]:
                    if element[1] % div[1] == 0:
                        counter += 1
            cur_divs = []

