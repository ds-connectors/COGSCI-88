# Import relevant libraries
#%matplotlib inline

import math
from scipy.special import erfc
import matplotlib.pyplot as plt
import numpy as np

wf1 = .3
wf2 = .17
wf3 = .11

n1 = np.arange(1, 101, 1)
n2 = np.add(1,n1)
m2 = np.add(10,n1)

lenarray = len(n1)

v1 = .5 * erfc (np.divide ( abs(np.subtract(n1,n2)), math.sqrt(2) * wf1 * np.sqrt(np.square(n1) + np.square(n2)) ))
v2 = .5 * erfc (np.divide ( abs(np.subtract(n1,n2)), math.sqrt(2) * wf2 * np.sqrt(np.square(n1) + np.square(n2)) ))
v3 = .5 * erfc (np.divide ( abs(np.subtract(n1,n2)), math.sqrt(2) * wf3 * np.sqrt(np.square(n1) + np.square(n2)) ))

u1 = .5 * erfc (np.divide ( abs(np.subtract(n1,m2)), math.sqrt(2) * wf1 * np.sqrt(np.square(n1) + np.square(m2)) ))
u2 = .5 * erfc (np.divide ( abs(np.subtract(n1,m2)), math.sqrt(2) * wf2 * np.sqrt(np.square(n1) + np.square(m2)) ))
u3 = .5 * erfc (np.divide ( abs(np.subtract(n1,m2)), math.sqrt(2) * wf3 * np.sqrt(np.square(n1) + np.square(m2)) ))

a=plt.figure()
plt.plot(range(lenarray), v1)
plt.plot(range(lenarray), v2)
plt.plot(range(lenarray), v3)
plt.xlabel('n1', fontsize=20)
plt.ylabel('Error prob.', fontsize=20)
plt.legend(['wf = .30 (children)', 'wf = .17 (munduruku)', 'wf = .11 (english)'], loc='lower right')
plt.title('n2 - n1 = 1')
plt.ylim([0, .5])

b=plt.figure()
plt.plot(range(lenarray), u1)
plt.plot(range(lenarray), u2)
plt.plot(range(lenarray), u3)
plt.xlabel('n1', fontsize=20)
plt.ylabel('Error prob.', fontsize=20)
plt.legend(['wf = .30', 'wf = .17', 'wf = .11'], loc='lower right')
plt.title('m2 - n1 = 10')
plt.ylim([0, .5])

