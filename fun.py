#!/usr/bin/env python
# coding: utf-8

# In[25]:


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
        An = (4*n)/(n**2 - 1)
    return An
    
sWave = np.zeros(np.shape(x))

for n in range(1,N+1):
    sWave = sWave + coeffSquare(n)*np.sin((n*x))

for n in range(1,N+1):
    y = coeffSquare(n)*np.sin((n*x))

plt.plot(x,y,'bo')
plt.plot(x,sWave)


# In[3]:


# Question 5
import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import scipy as sc
import sympy as sp

from matplotlib import animation, rc
from IPython.display import HTML

g,s,p,L,l,a = sp.symbols(['g','s','p','L','l','a'])

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

w = ((2*g*np.pi)/l + (8*np.pi**3*s)/(l**3*p))**(1/2) # Exactly from the sheet. 
wp = (sp.diff(w,l) - a) # dw/dl # The extra A term is for the solve function to get the Y value
wpp = sp.diff(w,l,l) #d^2w/dl^2


print("w: ",w,'\n\n w\':',wp,'\n\n w\'\':',wpp,'\n\n')
for i in range(0,len(sp.solve(wpp,l))):
    answer.append(((sp.solve(wpp,l)[i]))) # We may get complex solutions here, this is FINE. 

print("Extremum values: ", answer) # Solving second derivative gives four imaginary numbers...? These give l values. 
# Find minimum

q = []
i = 0
for i in range(0,len(sp.solve(wp,a))): 
    q.append(sp.solve(wp,a)[i])
    # We now have two arrays that correspond to 
    # l value in answer[i], wp value in 

    
l = answer[np.argmin(q)]    
l = abs(l)
z = l
wp1 = (-30.8190239317159/l**2 - 0.0174875400476891/l**4)*(61.6380478634317/l + 0.0116583600317927/l**3)**(-0.5)
print("MINIMUM: w' =",wp.subs('l',l),"m/s. . . \n\twhere lambda equals: ",l," meters")
vpmin = [abs(sp.im(l)),sp.im(np.amin(q).subs('l',l))] # But! We can only use positive lamba values. 

print(w,wp,wpp)

l = np.linspace(-10,L,N)

w1 = ((2*g*np.pi)/l + (8*np.pi**3*s)/(l**3*p))**(1/2)
wp1 = (-30.8190239317159/l**2 - 0.0174875400476891/l**4)*(61.6380478634317/l + 0.0116583600317927/l**3)**(-0.5)
wpp1 = (61.6380478634317/l**3 + 0.0699501601907564/l**5)*(61.6380478634317/l + 0.0116583600317927/l**3)**(-0.5) + (-30.8190239317159/l**2 - 0.0174875400476891/l**4)*(30.8190239317159/l**2 + 0.0174875400476891/l**4)*(61.6380478634317/l + 0.0116583600317927/l**3)**(-1.5)

wpz = (-30.8190239317159/z**2 - 0.0174875400476891/z**4)*(61.6380478634317/z + 0.0116583600317927/z**3)**(-0.5)

plt.xlim(-5,11)
plt.ylim(-1000,1000)
plt.plot(l,w1,'r--') # dispersion
plt.plot(l,wp1,'g--') # group velocity
plt.plot(l,wpp1,'b--') # change in group velocity over lambda 
plt.plot(z,wpz,'go')
plt.figure()

# Group velocity is a minimum when lambda = 0.35m, gv = -800m/s


# In[ ]:





# In[ ]:





# In[ ]:




