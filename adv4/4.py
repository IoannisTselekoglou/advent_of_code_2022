import csv

x = lambda a : int(a)

def input():
    csvfile = open("input.txt", "r")
    reader = csv.reader(csvfile, delimiter=",")
    return reader

def p1():
    ans = 0
    reader = input()
    for row in reader:
        a, b = row[0].split("-")
        c, d = row[1].split("-")

        l1 = [i for i in range(x(a),x(b)+1)]
        l2 = [i for i in range(x(c),x(d)+1)]

        if set(l1).issubset(l2) or set(l2).issubset(l1):
           ans += 1

    return ans

#print(p1())


def p2():
    ans = 0
    reader = input()
    for row in reader:
       a, b = row[0].split("-")
       c, d = row[1].split("-")

       l1 = [i for i in range(x(a),x(b)+1)]
       l2 = [i for i in range(x(c),x(d)+1)]

       for i in l1:
           if i in l2:
               ans += 1
               break

    return ans

print(p2())
