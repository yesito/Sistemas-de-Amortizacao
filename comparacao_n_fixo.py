# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 23:14:01 2021

@author: lucab
"""

import numpy as np
import matplotlib.pyplot as mt


k = 100
n = 15
i = np.linspace(0.01,5,k)
p = 1
fvl_sac = []
def fuv_sac(i,n,p):
    fv = p*(1+(i*((n+1)/2)))
    return fv
for g in range (0,k,1):
    fvl_sac += [fuv_sac(i[g],n,p)]
mt.plot(i,fvl_sac)


fvl_a = []
def fuv_a(i,n,p):
    fv = ((i*p)*(n-1)) + (p*(1+i))
    return fv

for g in range (0,k,1):
    fvl_a += [fuv_a(i[g],n,p)]
mt.plot(i,fvl_a)


fvl_p = []
def fuv_p(i,n,p):
    fv = n*p*((i*((1+i)**n))/(((1+i)**n)-1))
    return fv

for g in range (0,k,1):
    fvl_p += [fuv_p(i[g],n,p)]
mt.plot(i,fvl_p)

fvl_sap = []
def fuv_sap(i,n,p):
    p = p + p*i
    fv = (n*p*i)/(1-((1-i)**n))
    return fv

for g in range (0,k,1):
    fvl_sap += [fuv_sap(i[g],n,p)]
mt.plot(i,fvl_sap)

mt.legend(["SAC","S_AMERICANO","S_PRICE","SAP"])
mt.title("Parametros: " + "i = " + "[0%," + str(int(i[k-1]*100)) +"%]" + " n = " + str(n) +  " p = " + str(p))
mt.savefig("plot4.pdf")
mt.show()




