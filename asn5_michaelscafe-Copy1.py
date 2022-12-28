#!/usr/bin/env python
# coding: utf-8

# In[45]:


import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import scipy as sc
import sympy as sp

from matplotlib import animation, rc
from IPython.display import HTML

L = 1
N = 100
x = np.linspace(0, L, 1000)

def coeffSquare(n):
    if (n % 2) != 0:
        # odd number
        An = 0
    else:
        An = (2*n)/(n**2 - 1)
    return An
    
sWave = np.zeros(np.shape(x))

for n in range(1,N+1):
    sWave = sWave + coeffSquare(n)*np.sin((n*x))

for n in range(1,N+1):
    y = coeffSquare(n)*np.sin((n*x))

plt.plot(x,y,'bo')
plt.plot(x,sWave)


# In[44]:


# Question 5
import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import scipy as sc
import sympy as sp

from matplotlib import animation, rc
from IPython.display import HTML

g,s,p,L,l,a,k = sp.symbols(['g','s','p','L','l','a','k'])

g = 9.81
s = 0.047
p = 1000
L = 100
N = 10000

#bS = ((4*np.pi*g)/(l**3) + (96*np.pi**3*s)/(l**5*p))/(2*((2*np.pi*g)/l + (8*np.pi**3*s)/(l**3*p))**(1/2) - (-(2*np.pi*g)/(l**2) - (24*np.pi**3*s)/(l**4*p))**2/(4*((2*np.pi*g)/l + (8*np.pi**3*s)/(l**3*p))**(3/2)))

answer = []

# These are the three equations we are going to need to use to solve for the maximum velocity. 
# w is the dispersion relation for waves on the surface of water. (Provided)
# To find group velocity we need to take the derivative of the dispersion with respect to wavenumber. 
# Wavenumber itself is a function of wavelength, so we can substitute it and take the derivative w.r.t. l
# Then, to find the local minima and maxima of the velocity function we have to take the derivative AGAIN, 
# and set (w(l))'' = 0, solving for l. Then sub it back in to get the point. 

w = (g*k + ((s*(k**3))/p))**(1/2) # Exactly from the sheet. 
wp = (sp.diff(w,k) - a) # dw/dl # The extra A term is for the solve function to get the Y value
wpp = sp.diff(wp,k) #d^2w/dl^2


print("w: ",w,'\n\n w\':',wp,'\n\n w\'\':',wpp,'\n\n')
for i in range(0,len(sp.solve(wpp,k))):
    if (sp.sympify((sp.solve(wpp,k)[i])).is_real):
        if ((sp.solve(wpp,k)[i]) > 0):
            answer.append(((sp.solve(wpp,k)[i]))) # Only get real, positive solutions. 

print("Extremum values (FOR K NOT L): ", answer) # Solving second derivative gives  imaginary numbers...? These give l values. 
# Find minimum

k = min(answer)

print("MINIMUM: w' =",(wp.subs('k',((2*np.pi)/k))).subs('a',0),"m/s. . . \n\twhere lambda equals: ",(2*np.pi)/k," meters.")


l = np.linspace(-10,L,N)

plt.xlim(-5,11)
plt.ylim(-1000,1000)
plt.plot(l,w1,'r--') # dispersion
plt.plot(l,wp1,'g--') # group velocity
plt.plot(l,wpp1,'b--') # change in group velocity over lambda 
plt.figure()

# Group velocity is a minimum when lambda = 0.35m, gv = -800m/s


# In[ ]:





# In[ ]:





# In[ ]:




