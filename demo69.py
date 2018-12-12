def build(x, y):
    return lambda: x * x + y * y
res = build(3, 4)
print( res )
