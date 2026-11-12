def calculate(num):

    if num<=1:
        print("not prime")
        return
    
    for i in range(2,num):
        if num%i==0:
            print("not prime")
            return
    print("prime")
calculate(4)