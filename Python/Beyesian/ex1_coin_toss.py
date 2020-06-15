# 동전던지기
import scipy.stats as stats
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from IPython.core.pylabtools import figsize
%matplotlib inline
matplotlib.rc('font', family='Malgun Gothic')

figsize(11, 9)

dist = stats.beta
n_trials = [0, 1, 2, 3, 4, 5, 8, 15, 50, 1000]
data = stats.bernoulli.rvs(0.5, size=n_trials[-1])
x = np.linspace(0, 1, 100)

for k, N in enumerate(n_trials):
    sx = plt.subplot(len(n_trials) / 2, 2, k+1)
    plt.xlabel('$p$, the probabilty of heads', fontsize=13) \
        if k in [0, len(n_trials) - 1] else None
    plt.setp(sx.get_yticklabels(), visible=False)
    heads = data[:N].sum()
    y = dist.pdf(x, 1 + heads, 1 + N - heads)
    plt.plot(x, y, label="nums of toss : %d, \n nums of observation of heads : %d")
    plt.fill_between(x, 0, y, color='#348ABD', alpha=0.4)
    plt.vlines(0.5, 0, 4, colors='k', linestyles='--', lw=1)

    leg = plt.legend()
    leg.get_frame().set_alpha(0.4)
    plt.autoscale(tight=True)

plt.suptitle('posterior of bayesian update', y=1.02, fontsize=14)
plt.tight_layout()
