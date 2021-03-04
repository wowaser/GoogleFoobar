# Index = tple[0], number = tple[1]
def solution(l):
    for x,num in enumerate(l):
        l[x] = (x,num)
    counter = 0
    cur_divs = []
    for e in l:
        for ele in l[e[0]+1:]:

            if ele[1] % e[1] == 0:
                cur_divs.append(ele)
        for div in cur_divs:
            for element in l[div[0]+1:]:
                if element[1] % div[1] == 0:
                    counter+= 1

        cur_divs = []
    return counter



