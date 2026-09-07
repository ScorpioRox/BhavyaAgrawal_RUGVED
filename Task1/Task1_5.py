def fib(x):
    if x == 0:
         print(0)
    elif x == 1:
        print(1)
    else:
        a,b = 0,1
        for i in range(2,x):
            c = a + b
            a = b
            b = c
        print(c)


fib(int(input("Enter a number: ")))