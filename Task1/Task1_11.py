def grade_cole(s):
    l=0
    sen=0
    for i in s:
        if i.isalpha():
            l+=1
        elif i in ['.','!','?']:
            sen+=1
    w = len(s.split())
    print("Letters:",l)
    print("Words:",w)
    print("Sentences:",sen)
    g = 0.0588 * (l/w*100) - 0.296 * (sen/w*100) - 15.8
    print("Grade:",g)

s=input("Enter a string: ")
grade_cole(s)
