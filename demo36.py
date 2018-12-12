def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
person('mmmd',30)
person('mmmddd',30,city = "beijing")
person('mmmddd',30,gender='m',city = "beijing")