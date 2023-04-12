
import math
x,y,z = map(int,input().split())

def theater_square(n,m,a):
    final = math.ceil(n/a) * math.ceil(m/a)
    print(final)


theater_square(int(x),int(y),int(z))