# Fibbonaci's sequence
def solution_station_1(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 1
        b = 1
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b
    



