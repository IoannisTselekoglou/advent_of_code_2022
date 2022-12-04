A = {"X": 4, "Y": 8, "Z": 3}

B = {"X": 1, "Y": 5, "Z": 9 }

C = {"X": 7, "Y": 2, "Z": 6}



input_file = open("input.in","r")

def p1(f):
    summe = 0
    f = f.readlines()
    lines = [i.strip("\n") for i in f]
    lines = [i.replace(" ", "")  for i in lines]


    for i in lines:
        if i[0] == "A":
            summe += A[i[1]]
        if i[0] == "B":
            summe += B[i[1]]
        if i[0] == "C":
            summe += C[i[1]]
    return print(summe)




def p2(f):
    L = {"A" : (1,3,2),"B" : (2,1,3),"C" : (3,2,1)}
    summe = 0
    for i in f:
        a, b = i.split()
        if b == "Y":
            summe += L[a][0] + 3

        elif b == "X":
            summe += L[a][1]

        elif b == "Z":
            summe += L[a][2] + 6

        a = "ABC".index(a)
    return print(summe)

#p1(input_file)
p2(input_file)
