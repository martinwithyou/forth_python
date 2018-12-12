def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1,2,3,4,5,6,7,8)
print( f() )
f1 = lazy_sum(1,2,3,4,5,6,7,8)
f2 = lazy_sum(1,2,3,4,5,6,7,8)
print( f1 == f2 )