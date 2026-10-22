def fact(n):
    if n <= 1:                      #base case.
        return 1
    else:
        return n * fact(n-1)

#main program
f = int(input("Enter the number your want the factorial of:"))
factorial = fact(f)
print(str(f)+"! is:",factorial)
