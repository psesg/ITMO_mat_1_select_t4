import math

xmaX = 15
ymaX = 12
k = 0
x, y = 0, 0
for i in range(ymaX):
    for j in range(xmaX):
        x = x + (i - 1)
        y = y + (j - 1)
        k = k +1
        print(k,i,j)
print(x,y)
print(math.sqrt(x*x + y*y))
#answer: length sum of vectors = 1350