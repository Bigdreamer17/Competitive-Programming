def ginortS(a):
    if a.islower():
        return(1,a)
    elif a.isupper():
        return(2,a)
    elif a.isdigit() :
        if int(a)%2==1:
            return(3,a)
        else :
            return(4,a)

print(*sorted(input(),key=ginortS),sep='')