import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy 

x=[0.7,1.6,0.7,1.7,2.6,1.1,0.6,2.9]
y=[0.6442,0.9996,0.6442,0.9917,0.5155,0.8912,0.5646,0.2392]

#np.polyfit(x=x,y=y,deg)
p=sns.regplot(x=x,y=y,order=2)


p=slope, intercept, r, p, sterr = scipy.stats.linregress(x=p.get_lines()[0].get_xdata(),y=p.get_lines()[0].get_ydata())

plt.show()