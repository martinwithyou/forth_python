import pickle
d = dict(name='bob',age=20,score=88)
f = open('text.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('text.txt','rb')
d = pickle.load(f)
f.close()
print(d)