def sum_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)


#main program
num=int(input("Enter your number:"))
total=sum_digits(num)
print(total)
