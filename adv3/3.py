f = open("input.txt", "r")

abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def p1(f):
    ans = 0
    for i in f:
        x = int(len(i)/2)
        a = i[:x] , b = i[x:]
        for j in range(x):
            if a[j] in b:
                ans += abc.index(a[j]) + 1
                break
    return ans

def p2(f):
  ans = 0
  grp1 = []
  for i,j in enumerate(f):
      grp1.append(set(j.strip("\n")))
      if (i+1)%3 == 0:
        for i in grp1[0]:
          for j in i:
            if j in grp1[1] and j in grp1[2]:
                ans += abc.index(j) + 1
                break
        grp1 = []
  return ans

print(p2(f))
