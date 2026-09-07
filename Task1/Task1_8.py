def div_str(n):
    s = "abcdabcdabcdabcd"
    s = list(s)
    l = []
    for i in range(len(s)//n):
        x = ''
        for k in range(n):
            x = x + s[i*n + k]
        l.append(x)

    for j in l:
        if j != l[0]:
            print("The string cannot be divided into equal parts.")
            return

    print(l)

n = int(input("Enter n: "))

div_str(n)



