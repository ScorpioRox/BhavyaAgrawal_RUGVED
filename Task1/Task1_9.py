def ceasar(s,n):
    s = s.lower()
    s = list(s)
    for i in range(len(s)):
        if s[i].isalpha():
            x = ord(s[i]) + n
            if x > 122:
                x = x - 26
            s[i] = chr(x)
    for j in s:
        print(j, end="")

s = input("Enter a string: ")
n = int(input("Enter n: "))
ceasar(s,n)