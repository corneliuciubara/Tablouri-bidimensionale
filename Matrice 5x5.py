x=[[2,4,3,6,1],
   [3,5,4,7,2],
   [9,7,5,3,4],
   [1,3,6,4,2],
   [8,9,3,1,2]]


for i in range(0,len(x)):
    print('Suma elementelor pentru rîndul ',i,' : ',sum(x[i]))


# iteram dupa coloane
for i in range(0,len(x[0])):
    sumCol=0
    # iteram dupa randuri
    for j in range(0,len(x)):
        sumCol+=x[j][i]
    print('Suma elementelor pentru coloana ',i,' :',sumCol)


# iteram duparamduri
print('Diagonala principala:')
for i in range(0,len(x)):
    print(x[i][i],end=' ')
print()

# iteram duparamduri
print('Diagonala secundara:')
for i in range(0,len(x)):
    print(x[len(x)-1-i][i],end=' ')
print()