def sort_str(s):
    s = sorted(s)
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        elif i in d:
            d[i] += 1
    for i in s:
        print(i, end="")
    print()
    for i in d:
        print(i, ':', d[i])

sort_str(input("Enter a string: "))