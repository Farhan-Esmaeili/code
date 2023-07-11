#input
sec = int(input("Please write your input(in secounds) : "))

#intializing
min = sec//60
sec_total = sec % 60
min_total = min % 60
hour_total = min // 60

#output
print(hour_total,":", min_total, ":", sec_total)

# Farhan Esmaeili | newbie programmer
