#function for conversion celsius to farnhenheit
def celsius_to_farn(cel):
    F = cel * (9/5) + 32
    return F

#procedure for table

def conversion_table(start,end,step):
    print("Celsius        Farhenheit")
    for c in range(start,end+1,step):
        print(f"{c:<10}{celsius_to_farn(c)}")


#main program
c = float(input("Enter celsius value"))
far=celsius_to_farn(c)
print(far)
conversion_table(0,50,10)
