try:
    f = open('./test.txt')
    print(f.read())
finally:
    if f:
        f.close()