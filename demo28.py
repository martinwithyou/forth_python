# import match
def move(x,y,step,angle=0):
    nx = x + step * 100+angle
    ny = y - step * 100+angle
    return nx, ny
x,y = move(100,100,60,99)
print(x,y)
