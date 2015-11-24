#%matplotlib inline

# Import relevant libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pylab as P

nsamp = 10000

a = np.arange(0,180,20)
t = [1.1,  1.6,  2. ,  2.3,  2.5,  3. ,  3.5,  3.8,  4.3]

# t = 4.6 for 180

lena = len(a)
ind = np.arange(0,lena)

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(a,t)

print('p-value = ',p_value)
print('r2 = ',r_value)

# Visualize data fit
plt.scatter(a,t,color='black');
plt.plot(a,a*slope+intercept)
plt.xlabel('Angle', fontsize=20)
plt.ylabel('Mean reaction time (sec)', fontsize=20)


# Sample with replacement
slopebst = [0]*nsamp

for i in range(0,nsamp):
    sampleinds = np.random.choice(ind,size=lena)
    rtsample = np.arange(0,lena)
    for idx in sampleinds:
        rtsample[idx] = t[sampleinds[idx]]
    ss, ii, rr, pp, dd = stats.linregress(a[sampleinds],rtsample)
    slopebst[i] = ss

# Histogram the randomized slopes and compare the observed slope to the randomized slopes
P.figure()
n, bins, patches = P.hist(slopebst, 100)

ci = np.std(slopebst)/np.sqrt(nsamp)*1.96

pred = 180*slope+intercept

print("bootstrapped mean slope = ",np.mean(slopebst))
#print("bootstrapped standard error = ", ci)
print("observed slope = ",slope)
print("predicted RT = ",pred)
print("actual RT = ",4.6)


P.show()

plt.show()



