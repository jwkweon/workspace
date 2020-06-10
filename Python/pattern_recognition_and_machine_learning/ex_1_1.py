import numpy as np
import matplotlib.pyplot as plt
import math


def get_training_n_target_set(num, mu, sigma):
    diff = 1/(num-1)
    x = [i*diff for i in range(num)]

    target = get_target_data(x)
    gaussian_noise = np.random.normal(mu, sigma, num)
    train = target + gaussian_noise

    train_set = np.array([[x, y] for x, y in zip(x, train)])
    target_set = np.array([[x, y] for x, y in zip(x, target)])

    return train_set, target_set


def get_target_data(x_list):
    PI = np.pi
    target = [np.sin(i*PI) for i in x_list]
    return target

# trainset[:, 1:]


trainset, targetset = get_training_n_target_set(10, 0, 0.3)
plt.plot(trainset[:, 1:], linewidth=2, color='r')
plt.plot(targetset, linewidth=2, color='b')

trainset[:, 0:-1]


plt.plot(m, linewidth=2, color='r')
plt.show()

np.random.seed(100)
noise = np.random.normal(size=10, )
noise

np.random.multivariate_normal(any)

mu, sigma = 0, 0.3  # mean, standard deviation
sample_num = 10
gaussian_noise = np.random.normal(mu, sigma, sample_num)

# sample들의 historgram을 출력한다.
count, bins, ignored = plt.hist(gaussian_noise, 30, normed=True)
# sample들을 이용해서 Gaussian Distribution의 shape을 재구축해서 line으로 그린다.
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
         np.exp(- (bins - mu)**2 / (2 * sigma**2)), linewidth=2, color='r')
plt.show()
