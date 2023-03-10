from scipy.stats import poisson,norm,ttest_ind
import numpy as np
import matplotlib.pyplot as plt


#----Poisson Distribution (Discrete) tests----
x = np.arange(1,10)
mu=3

p_distr=poisson.pmf(x,mu)
p_cumml=poisson.cdf(x,mu)
p_sample=poisson.rvs(mu, size=1000)

fig,ax=plt.subplots()
ax.set_title("poisson")
ax.hist(p_sample,density=True)
ax.scatter(x,p_distr,c="r")
ax.scatter(x,p_cumml,c='g')
plt.show()
#the start of the bins fit with the theoretical values from poisson dist as they should

#----Standard(mu=0,sigam=1) Normal Distribution (Continuous) tests----
x = np.arange(-3,3,0.02)

n_distr=norm.pdf(x)
n_cumml=norm.cdf(x)
n_sample=norm.rvs(size=1000)

fig,ax=plt.subplots()
ax.set_title("std normal")
ax.hist(n_sample,density=True)
ax.scatter(x,n_distr,c="r")
ax.scatter(x,n_cumml,c='g')
plt.show()
#the start of the bins fit with the theoretical values from poisson dist as they should


#-----testing the samples---
n_sample2=norm.rvs(size=1000) #another sample from norm

print(ttest_ind(n_sample,n_sample2))
print(ttest_ind(n_sample,p_sample))

