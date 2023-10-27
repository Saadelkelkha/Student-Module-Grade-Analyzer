t=[]
for i in range (5):
    l=[]
    for j in range (3):
        print("enter the mark of the student n",i+1,"of the module ",j+1)
        n=float(input())
        l.append(n)
    t.append(l)
for i in range (5):
    S=0
    for j in range (3):
        S=S+t[i][j]
    M=S/3
    print("the average of the student n",i+1,"is :",M)
for j in range (3):
    max = t[0][j]
    min = t[0][j]
    for i in range(5):
        if max<t[i][j] :
            max=t[i][j]
        if min>t[i][j] :
            min>t[i][j]
    print("the maximum mark in the modul ",j+1,"is",max)
    print("the minimum mark in the modul ",j+1,"is",min)