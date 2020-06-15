# librarian? or farmer?
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from IPython.core.pylabtools import figsize
%matplotlib inline
matplotlib.rc('font', family='Malgun Gothic')

figsize(12.5, 4)
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.dpi'] = 300

colors = ['#348ABD', '#A60628']
prior = [1/21., 20/21.]
posterior = [0.087, 1-0.087]
plt.bar([0, .7], prior, alpha=0.70, width=0.25,
        color=colors[0], label='prior', lw='3', edgecolor='#348ABD')

plt.bar([0+0.25, .7+0.25], posterior, alpha=0.70, width=0.25,
        color=colors[1], label='posterior', lw='3', edgecolor='#A60628')

plt.xticks([0.20, 0.95], ['librarian', 'farmer'])
plt.title('prior, posterior of job')
plt.ylabel('probabilty')
plt.legend(loc='upper left')
