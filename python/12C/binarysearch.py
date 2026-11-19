items=[102,118,125,139,147,156,163,178,184,199]
target=163
count=1
lowerindex = 0
higherindex=len(items)-1

while lowerindex <= higherindex:
    middleindex = (lowerindex + higherindex)//2
    if items[middleindex] == target:
        print("found after",count,"checks")
        break
    elif items[middleindex] > target:
        higherindex = middleindex - 1
        count=count+1
    else:
        lowerindex = middleindex + 1