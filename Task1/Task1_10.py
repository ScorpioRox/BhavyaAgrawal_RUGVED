def card(n):
    n = n[::-1]
    t = 0
    for i in range(len(n)):
        x = int(n[i])
        if i % 2 == 1:
            x = x * 2
            if x > 9:
                x = x - 9
        t = t + x

    if t % 10 == 0:
        print("Valid.")
    else:
        print("Invalid.")

card(input("Enter a card number: "))