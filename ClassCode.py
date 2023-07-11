
#input
num = int(input("Write number of students : "))
max=0
min = 1000
min_num=0
sum=0
a=0
for i in range(num):
    k=i+1
    print("Write number", k , "student score ")
    score = float(input("score :"))
    sum += score
    #intializing
    if max < score :
        max = score
        max_num = k
    if min > score :
        min = score
        min_num = k
avarage = sum / num
#output
print("The avarage of all class is", avarage ,".")
print("Maximum grade was the grade of student number", max_num , "with the grade", max)
print("Minimum grade was the grade of student number", min_num , "with the grade", min)

# Farhan Esmaeili | newbie programmer