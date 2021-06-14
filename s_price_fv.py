# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 23:14:01 2021

@author: lucab
"""

import numpy as np
import mayavi.mlab as plt

k = 100
n = []
for i in range (0,k,1):
    n += [i]
    
i = np.linspace(0.01,5,15)
nv,iv = np.meshgrid(n,i, indexing = "ij", sparse = False)
p = 1
fv = nv*p*((iv*((1+iv)**nv))/(((1+iv)**nv)-1))

plt.figure (1,fgcolor= (0,0,0), bgcolor = (1,1,1))
plt.surf(nv,iv*10,fv/10, representation = "wireframe")
#warp_scale = "auto" changes axes scale. That is why if you print the axes they will seem to have wrong values.
plt.axes(xlabel = "n",ylabel = "i",zlabel = "FV", nb_labels = 3, color = (0,0,0))
plt.title("fv(n,i)", size = 0.4)
plt.show()