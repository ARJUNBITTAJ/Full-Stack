num =150

if num<=1:
    print("not prime number")
else:
    is_prime = True

    for i in range(2,num):
        if num%2==0:
            print(" it is not prime")
            is_prime= False
            break

if is_prime:
    print("it is prime")
        