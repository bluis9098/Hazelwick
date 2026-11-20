score = 0

def add_points(points):
    bonus = 5
    total = points+bonus
    return total

def add_to_score(score,points):
    return score+points

result = add_points(10)
print(result)
score = add_to_score(score,result)
print(score)
print(bonus)