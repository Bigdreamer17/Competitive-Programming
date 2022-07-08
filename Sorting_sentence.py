a = input("Enter the sentence: ").split()
a.sort(key = lambda x: x[-1])
print("Sorted sentence:",' '.join([i[:-1] for i in a]))

   