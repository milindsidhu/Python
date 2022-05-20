inp = int(input("Enter a number:\n"))
summ = 0

while inp > 0:
    summ = summ + inp % 10
    inp = inp // 10

print(summ)

