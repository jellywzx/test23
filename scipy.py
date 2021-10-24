# test1
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats


def normal(power, mean, std, val):
    a = 1/(np.sqrt(2*np.pi)*std)
    diff = np.abs(np.power(val-mean, power))
    b = np.exp(-(diff)/(2*std*std))
    return a*b

pdf_array = []
array = np.arange(-2,2,0.1)
print array
for i in array:
    print i
    pdf = normal(2, 0, 0.1, i)
    print pdf
    pdf_array.append(pdf)

plt.plot(array, pdf_array)
plt.ylabel('some numbers')
plt.axis([-2, 2, 0, 5])
plt.show()


# # test2
# from scipy.stats import  hypergeom
# import numpy as np
# [M,n,N]=[20,7,12]
# x=np.arange(4)*2
# prb = hypergeom.cdf(x,M,n,N)
# hypergeom.ppf(prb,M,n,N)

# # 实现正态分布
# import numpy as np
# from scipy import stats
# import matplotlib.pyplot as plt
# mu=0
# sigma=1
# x=np.arange(-5,5,0.1)
# plist= stats.norm.pdf(x,mu,sigma)
# plt.plot(x,plist)
# plt.show()

# test3
import random
a=[]
for i in range(1000):
    a.append(random.randint(20,100))
b=sorted(a)
c=dict()
for i in b:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print(c)