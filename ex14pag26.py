n=[[1,2,3,4,5],
   [8,1,2,7,6],
   [3,5,1,4,1],
   [4,1,3,7,8],
   [3,7,2,3,5]]
#a
print('a) suma componentelor pe diagonala principala:')
a = 0
for i in range(0,len(n)):
    a += n[i][i]
  
print(a)

#b
print('b) suma componentelor pe diagonala secundara:')
b = 0

for j in range(0,len(n)):
    b += n[len(n)-1-j][j]

print(b)

#c
print('c) suma componentelor mai sus de diagonala principala:')
c = 0
for i in range(0,len(n)):
    for j in range(i+1,len(n)):
        c += n[i][j]

print(c)
#d
print('d) suma componentelor mai jos de diagonala principala:')
d = 0
for i in range(0,len(n)):
    for j in range(0,i):
        d += n[i][j]

print(d)

#e
print('e) suma componentelor mai sus de diagonala secundara:')
e = 0
for i in range(0,len(n)):
    for j in range(j+1,len(n)):
        e += n[i][j]

print(e)

#f
print('f) suma componentelor mai jos de diagonala secundara:')
f = 0
for i in range(0,len(n)):
    for j in range(0,j):
        f += n[i][j]

print(f)

