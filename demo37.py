def person(name,age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name,'age:',age,'other:',kw)

person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)