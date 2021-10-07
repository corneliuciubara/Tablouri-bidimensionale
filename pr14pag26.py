x=[[2,4,3,6,1],
   [3,5,4,7,2],
   [9,7,5,3,4],
   [1,3,6,4,2],
   [8,9,3,1,2]]
#a
print('suma componentelor pe diagonala principala:')
sumDiagp = 0
for i in range(0,len(x)):
    sumDiagp += x[i][i]
  
print(sumDiagp)

#b
print('suma componentelor pe diagonala secundara:')
sumDiags = 0

for j in range(0,len(x)):
    sumDiags += x[j][j]

print(sumDiags)

#c
print('suma componentelor mai sus de diagonala principala:')

sumDeasuprap = 0
for i in range(0,len(x)):
    for j in range(0,len(x[0])):
        sumDeasuprap += x[i][j]

print(sumDeasuprap)



#d
print('suma componentelor mai jos de diagonala principala:')

sumDeasupras = 0
for i in range(0,len(x[0])):
    for j in range(0,len(x)):
        sumDeasupras += x[i][j]
print(sumDeasupras)

#e
print('suma componentelor mai sus de diagonala secundara:')
sumsusS = 0
for i in range(0,len(x[0])):
    for j in range(0,len(x)):
        sumsusS += x[i][j]
print(sumsusS)


#f
print('suma componentelor mai jos de diagonala secundara:')
sumjosS = 0
for i in range(0,len(x[0])):
    for j in range(0,len(x)):
        sumjosS += x[i][j]
print(sumjosS)