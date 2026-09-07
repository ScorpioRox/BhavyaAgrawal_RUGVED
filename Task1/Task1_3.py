def hill_no(x):
    l = []
    a = 0
    increase = True
    for i in x:
        l.append(int(i))
    for k in l:
        if increase:
            if k >= a:
                a = k
            else:
                increase = False
                a = k
        elif not increase:
            if k <= a:
                a = k
            else:
                return False
    return True

print(hill_no(input("Enter a number: ")))