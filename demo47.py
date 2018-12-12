# print( list(range(1,11)) )
L = []
for x in range(1,11):
    L.append(x * x)
print( L )
print( [x * x for x in range(1,11)] )
print( [x * x for x in range(1,11) if x % 2 == 0 ] )