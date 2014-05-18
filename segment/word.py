#encoding=utf-8
f = open('D:\Study\Video\segment\gamedict.txt' , encoding='utf-8')
f2 = open('D:\Study\Video\segment\gamedict2.txt' , mode='w',encoding='utf-8')
L = []
for line in f:
    #print(line)
    T = line.split(u'，')
    for x in T:
        L.append(x.strip())
print(L)
for w in L:
    f2.write(w+' 1 n \n')
f.close()
f2.close()
