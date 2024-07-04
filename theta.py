import numpy as np
import math as mt

k = 29
rad = mt.radians(k)
pxtheta = rad/240
print(pxtheta)
pxk = mt.degrees(pxtheta)
print(pxk)

i=1
cos0 = np.arange(480 ,dtype=float)
cos=np.cos(rad)
cos0[0] = cos
print(cos0[0])
r=rad-pxtheta
while 480>i:
    print(cos0[i-1])
    print(r)
    if 239>i:
        r=r-pxtheta
    else:
        r=r+pxtheta
    cos=np.cos(r)
    cos0[i]=cos
    i = i+1