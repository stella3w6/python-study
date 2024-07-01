burger = int(input())
drink = int(input())
side = int(input())
dessert = int(input())

sum = 0

if burger == 1:
    sum = sum + 461
elif burger == 2:
    sum = sum + 431
elif burger == 3:
    sum = sum + 420
elif burger == 4:
    sum = sum
    
if drink == 1:
    sum = sum + 130
elif drink == 2:
    sum = sum + 160
elif drink == 3:
    sum = sum + 118
elif drink == 4:
    sum = sum
    
if side == 1:
    sum = sum + 100
elif side == 2:
    sum = sum + 57
elif side == 3:
    sum = sum + 70
elif side == 4:
    sum = sum
    
if dessert == 1:
    sum = sum + 167
elif dessert == 2:
    sum = sum + 266
elif dessert == 3:
    sum = sum + 75
elif dessert == 4:
    sum = sum
    
print("Your total Calorie count is " + str(sum) +".")