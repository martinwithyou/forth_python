from functools import reduce
def fn(x,y):
    return  x * 10 + y

res = reduce( fn, [1,2,3,5,7,9])
print(res)