Numbers = int(input("Type a number greater than 1 and I will give you a sum of all the even numbers: "))

Number_list = []

for x in range(0, Numbers + 1):
    Number_list.append(x)

Total = 0
for var in Number_list:
    if Number_list[var] % 2 == 0:
        Total += Number_list[var]
print(Total)