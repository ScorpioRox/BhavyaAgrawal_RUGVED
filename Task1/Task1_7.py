def fib(x):
    a,b = 0,1
    if x == 1:
         print(a)
    elif x == 2:
        print(a,b)
    else:
        print(a, b, end=" ")
        for i in range(2,x):
            c = a+b
            a = b
            b = c
            print(c, end=" ")


fib(int(input("Enter a number: ")))