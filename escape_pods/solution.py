def solution(en, ex, path):
    INF = 2000001

    def retrace(parents_lst):
        cur = parents_lst[-1]
        path = [parents_lst[-1]]
        while 0 not in cur:
            cur = [e for e in parents_lst if e[1] == cur[0]][0]
            path.append(cur)
        return path

    if len(en) > 1:
        start_row = [0] * len(path)
        for y in en:
            start_row[y] = INF
        path.insert(0, start_row)
        for row in path:
            row.insert(0, 0)
        ex = [x + 1 for x in ex]
        en = [0]

    if len(ex) > 1:
        last_row = [0] * len(path)
        path.insert(-1, last_row)
        for i, row in enumerate(path):
            if i in ex:
                value = INF
            else:
                value = 0
            row.append(value)
        ex = [len(path) - 1]

    tot_flow = 0
    while True:
        vis = []
        parents = []
        q = [en[0]]
        cur_nod = None
        while ex[0] not in vis:
            if q:
                cur_nod = path[q[0]]
                if q[0] not in vis:
                    vis.append(q[0])
                for i, e in enumerate(cur_nod):
                    if e != 0 and i not in vis:
                        q.append(i)
                        vis.append(i)
                        way = (q[0], i)
                        parents.append(way)
                q.pop(0)

            elif not q:
                return tot_flow
        way = retrace(parents)
        flow = min([path[x[0]][x[1]] for x in way])
        for ele in way:
            path[ele[0]][ele[1]] -= flow
            path[ele[1]][ele[0]] += flow
        tot_flow += flow
