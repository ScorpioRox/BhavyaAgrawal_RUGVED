def anagram(s1,s2):
    if sorted(s1) == sorted(s2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
anagram(s1,s2)
