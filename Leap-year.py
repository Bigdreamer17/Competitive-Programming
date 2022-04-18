def is_leap(year):
    if year % 4 == 0 and year % 400 == 0:
        print ("True")
    elif year % 100 == 0:
        print ("False")
   
    
year = int(input("Enter year: "))
is_leap(year)