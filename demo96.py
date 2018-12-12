from io import StringIO
f = StringIO("go,go,go,go")
while True:
    s = f.readline()
    if s == "":
        break
    print(s.strip())