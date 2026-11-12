def calculation():
    result=0
    n1=int(input("enter the 1st number"))
    n2=int(input("enter the 2nd number"))
    operation =int(input("press 1 for addition or press 2 for substraction"))
    if operation==1:
        result=n1+n2
        print(result)
    elif operation==2:
        result=n1-n2
        print(result)
calculation()
