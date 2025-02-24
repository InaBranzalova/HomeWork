# Task
# Calculate your body mass index (BMI) with Python, given the formula:
# BMI = W / (H*H)
# where:
# W = weight_in_kilogram
# H = height_in_meters

W = 61
H = 161
BMI = W / (H * H)
print(BMI)
print(round(BMI , 2))
print(round(BMI,3))



W = int(input('Enter weight in kg :   '))
print(W)
H = int(input('Enter your hight in sm :   '))
print(H)
BMI = (W/(H*H))
res = round(BMI,2)
print("Your body mass index is ", res)