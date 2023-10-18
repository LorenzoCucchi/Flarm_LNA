import numpy as np
from float2SI import float2SI

R = 50
f = np.linspace(860*10**6,880*10**6,num=100)
fw = 868.3*10**6

#n=13.2

n = 13.1

X_c = R/n
X_L = R*n

C = 1/(2*np.pi*fw*X_c)
L = X_L/(2*np.pi*fw)

print("C: ", f"{float2SI(C)}F")
print("L: ", f"{float2SI(L)}H")

C_a = 48*10**(-12)
L_a = 120*10**(-9)

Xc_a = 1/(2*np.pi*fw*C_a)
XL_a = L_a*(2*np.pi*fw)

nc = R/Xc_a
nl = XL_a/R

print("nc :", nc)
print("nl :", nl)
