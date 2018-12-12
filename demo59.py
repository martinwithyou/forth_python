def not_empty(s):
    return s and s.strip()

res = list(filter(not_empty, ['a','','b',None,'c',''] ))

print( res)