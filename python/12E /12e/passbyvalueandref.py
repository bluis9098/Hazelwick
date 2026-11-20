def double_number(n):
    n=n*2
    print("Inside procedure:",n)

def double_list(values):
    for i in range(len(values)):
        values[i] = values[i]*2
    print("Inside procedure:",values)

#main program
number = 5
double_number(number)
print("After call:",number)

numbers = [1,2,3]
double_list(numbers)
print("After call:",numbers)