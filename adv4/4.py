import csv

x = lambda a : int(a)

def input():
    csvfile = open("input.csv", "r")
    reader = csv.reader(csvfile, delimiter=",")
    return reader

def p1():
    ans_1 = 0 ; ans_2 = 0
    reader = input()
    for row in reader:
        a, b = row[0].split("-")
        c, d = row[1].split("-")
        l1 = [i for i in range(x(a),x(b)+1)]
        l2 = [i for i in range(x(c),x(d)+1)]

        if set(l1).issubset(l2) or set(l2).issubset(l1):
           ans_1 += 1

        #part 2
        for i in l1:
          if i in l2:
            ans_2 +=1
            break
    return ans_1, ans_2


print(p1())


