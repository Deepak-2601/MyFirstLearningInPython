num_days = int(input("How many day's temperature?: "))
total = 0
temp = []
for i in range(num_days):
    next_days = int(input("Days " + str(i+1) + "'s high temperature: "))
    temp.append(next_days)
    total += temp[i]

avg = round(total / num_days, 2)
print("\nAverage=" + str(avg))
above = 0
for x in temp:
    if x > avg:
        above += 1

print(str(above) + "day(s) above average ")
