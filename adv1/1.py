import csv


y = 0
results = []
with open("input1.csv") as csvfile:
    reader = csv.reader(csvfile)
    for i in reader:
        try:
            y += int(i[0])
        except:
            results.append(y)
            y = 0

#results.sort(reverse=True)

results.sort()

y = results[::-1]

y_2 = 0
for i in range(3):
    y_2 += y[i]
print(y_2)





