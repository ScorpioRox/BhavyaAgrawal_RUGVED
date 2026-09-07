def selec_sort(s):
    s = list(s)
    new_s=''
    for k in range(len(s)):
        x = s[0]
        for i in s:
            if i < x:
                x = i
        new_s += x
        s.remove(x)
    return new_s

s = input("Enter a string: ")
print("Sorted string:", selec_sort(s))