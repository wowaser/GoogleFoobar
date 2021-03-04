def solution(tot):
    def fibonacci(n):
        lst = [1, 1]
        for i in range(n - 2):
            lst.append(lst[-1] + lst[-2])
        return lst

    def max_henchmen(n):
        lst = [1]
        while sum(lst) < n:
            if sum(lst) + lst[-1] * 2 > n:
                break
            lst.append(lst[-1] * 2)

        return len(lst)

    for k in range(45):
        lst = fibonacci(k)
        if sum(lst) <= tot and sum(fibonacci(k + 1)) > tot:
            break
    stingy = len(lst)
    double = max_henchmen(tot)

    return abs(stingy - double)
