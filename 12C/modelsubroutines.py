#function 1: Celsius to farn converter
def celsius_to_farn(celsius):
    F = celsius * (9/5) + 32
    return F

#procedure 1 conversion table
def print_conversion_table(start,end,step):
    print("Celsius  Fahrenheit")
    for i in range(start,end+1,step):
        print(f"{i:<10}{celsius_to_farn(i)}")




#main program
start = int(input("Enter start value:"))
end = int(input("End value:"))

print_conversion_table(start,end,10)


