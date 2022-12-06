f = open("input.txt")
s = open("map.txt")
l = []
for row in s:
    row = row.strip("\n")
    l.append(list(row.replace(",","")))


def p1(f):
    for i in f:
        x = i.split()
        m = int(x[1]);f = int(x[3])-1; t = int(x[5])-1
        for i in range(m):
            l[t].insert(0, l[f][0])
            l[f].pop(0)
    return "".join([i[0] for i in l if len(i)>0])

#print(p1(f))

def p2(f):
    for i in f:
        x = i.split()
        m = int(x[1]);f = int(x[3])-1; t = int(x[5])-1
        cringe = []
        for i in range(m):
            cringe += l[f][0]
            l[f].pop(0)
        l[t] = cringe + l[t]
    return "".join([i[0] for i in l if len(i)>0])


print(p2(f))


