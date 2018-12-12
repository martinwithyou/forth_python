import pickle
d = dict(name = 'bob',age = 20, score=88 )
res = pickle.dumps(d)
print( res )