d = { 'x':'A', 'y':'B', 'z':'C'}
for k, v in d.items():
    print(k, '=', v)

dd = { 'x':'A','y':'B','z':'C'}
print( [k + '=' + v for k, v in d.items()])

LL = [ 'Hello', 'World','IBM','Apple']
print( [s.lower() for s in LL ] )