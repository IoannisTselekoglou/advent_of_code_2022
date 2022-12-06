f = open("input.txt")
s = []
l = [[],["V","C","D","R","Z","D","B","W"], 
     ["G","W","F","C","B","S","T","V"],
     ["C","B","S","N","W"],
     ["Q","G","M","N","J","V","C","P"],
     ["T","S","L","F","D","H","B"],
     ["J","V","T","W","M","N"],
     ["P","F","L","C","S","T","G"],
     ["B","D","Z"],
     ["M","N","Z","W"]]

def p1(f,l): 
    print(l) 
    for i in f:
        s.append([int(s) for s in i.split() if s.isdigit()])
    for i in s:
        x = i[0]; y = i[1] ;z = i[2]  
        #part 1
        ass = ""
        for j in range(x):
            cringe += l[y][-1]
            l[y] = l[y][:-1]
        ass = ass[::-1]
        l[z] += cringe
        print(l)
    print("".join([i[len(i)-1] for i in l if len(i) > 0]))


def p2(f,l):
        
        for i in f:
          s.append([int(s) for s in i.split() if s.isdigit()])

        for i in s:
            x = i[0]; y = i[1] ;z = i[2]  
            move = l[y][:x]
            l[y] = l[y][x:]
            l[z] = move + l[z] 
        print("".join([i[0] for i in l if len(i) > 0]))


p1(f,l)
