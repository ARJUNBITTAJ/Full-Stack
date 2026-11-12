#Print all odd numbers between two given numbers.
fn = int(input("enter the number"))
sn = int(input("enter the end number"))
for i in range(fn,sn):
    if i%2!=0:
        print(i)

    