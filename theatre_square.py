from math import ceil
a,b,c = map(int,input().split())
d = ceil(a/c)
e = ceil(b/c)
print(e*d)
