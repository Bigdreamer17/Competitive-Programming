import re
  
  
for _ in range(int(input())):
    try:
        T = input()
        re.compile(T)
        print("True")
    except re.error:
        print("False")
    
  

