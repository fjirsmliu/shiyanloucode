for a in range(1,101):
    b = a % 7
    c = a % 10
    d = a // 10
    if b == 0 or c == 7 or d == 7:
        continue
    print(a)
