def swap(s):
    s = s.split(" ")
    b = '-'.join(s)
    return b
s = input("Enter a sentence: ")
print(swap(s))