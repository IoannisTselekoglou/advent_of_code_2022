x = open("input.txt","r")
data = str(x.read())

def p1(f,len_input):
    buffer = ""
    i = 0
    while i < len(f):
        if f[i] not in buffer:
            buffer += f[i]
            i += 1
            if len(buffer) == len_input:
                return i
        else:
            i -= len(buffer)
            buffer = ""
            i += 1

#print(p1(data,14))


