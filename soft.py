import numpy as np

def range(x,minx,maxx):
    scaleDef = 1
    rangeDef = 8
    scale = rangeDef/(maxx - minx)
    avg = maxx - (maxx - minx)/2
    x = x - avg
    y = np.exp(x*scale)/(1+np.exp(x*scale))
    return y


def peak(x,minx,center1,center2,maxx):
    y1 = range(x,minx,center1)
    y2 = range(x,maxx,center2)
    y = np.min([y1,y2],axis=0)
    return y



#x = np.array([y/10.0 for y in list(range(0,100,5))])
#x = x  - max(x)/2
#z = softpeak(x,-4,0,0,4)

#import matplotlib.pyplot as plt
#plt.plot(x, z)
