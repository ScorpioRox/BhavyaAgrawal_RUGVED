def triple_and (x, y, z):
    if bool(x) and bool(y) and bool(z):
        return True
    else:
        return False

print(triple_and(int(input("Enter first value: ")), int(input("Enter second value: ")), int(input("Enter third value: "))))
