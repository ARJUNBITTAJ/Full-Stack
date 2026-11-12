def calculate():
    string = "this a Hopping system"
    upper_count=0
    lower_count=0
    for i in string:
        if i.isupper():
            upper_count += 1
        elif i.islower() and i != " ":
            lower_count += 1
    print(f"upper_count={upper_count}")
    print(f"lower_count={lower_count}")

calculate()