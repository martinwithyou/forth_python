def createCounter():
    def counter():
        return 1
    return counter

print( createCounter()() )