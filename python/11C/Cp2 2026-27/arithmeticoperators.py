seconds = int(input("Enter your time in seconds:"))

hours = seconds // 3600
remaining = seconds % 3600
minutes = remaining // 60
seconds = remaining % 60
print(str(hours)+ " hours " + str(minutes)+ " minutes "+str(seconds)+" seconds ")