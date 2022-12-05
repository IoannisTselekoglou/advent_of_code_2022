import csv


f = open("input.txt")


def p1(f):
  y = 0
  results = []
  for i in f:
    try:
      y += int(i)
    except:
      results.append(y)
      y = 0
  return results

#print(max(p1(f)))

def p2(f):
  y = 0
  int_t = p1(f)
  int_t.sort(reverse=True)
  for i in range(3):
    y += int_t[i]
  return y

print(p2(f))





