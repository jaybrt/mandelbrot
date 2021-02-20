import matplotlib.pyplot as plot
import numpy as np

def iter_converge(c, thresh = 10, max_iter = 25):
    z = c
    i = 1
    while i < max_iter and (z*z.conjugate()).real < thresh:
        #print(i, z, c)
        z = z*z + c
        i+=1

    return i

def plotter(n, thresh = 10, max_iter = 25):
    '''
    This zooms in on one of the little arms
    mx = .1 / (n-1)
    my = .154 / (n-1)
    mapper = lambda x,y : (mx*x - 1.3, my*y - .474)
    '''
    mx = 2.48 / (n-1)
    my = 2.26 / (n-1)
    mapper = lambda x,y : (mx*x - 2, my*y - 1.13)
    img = np.full((n,n), 255)

    for x in range(n):
        for y in range(n):
            iter = iter_converge(complex(*mapper(x,y)), thresh = thresh, max_iter = max_iter)
            img[y][x] = 255 - iter

    return img

img = plotter(1000, thresh = 4, max_iter  = 40)
plot.imshow(img, cmap = 'magma')
plot.axis('off')
plot.show()
