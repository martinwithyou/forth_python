def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()

a = f1()
b = f2()
c = f3()

print(a,b,c)