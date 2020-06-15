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


def init_w(num):
    w = np.random.normal(size=num)

    return w


def get_polynomial(degree, w, x):
    hypothesis = []
    for j in x:
        result = 0
        for i in range(degree+1):
            result += w[i] * (j ** i)
        hypothesis.append(result[0])

    return hypothesis


def get_error(degree, w, x, t):
    error = 0.5 * np.sum((get_polynomial(degree, w, x) -
                          np.transpose(t[:, 1:])) ** 2, axis=-1)
    error = 0.5 * (get_polynomial(degree, w, x) - np.transpose(t[:, 1:])) ** 2
    return error


def get_diff(degree, w, x, t):
    diff = get_polynomial(degree, w, x) - np.transpose(t[:, 1:])
    return diff


def update_w(degree, w, x, t):
    print('w', w)
    print('diff', get_diff(degree, w, x, t))
    new_w = 0
    return new_w


w = [1, 2, 3]
x = [1, 2, 3]
np.array(w)*np.array(x)


if name == '__main__':
    mu, sigma = 0, 0.3  # mean, standard deviation
    sample_num = 10
    degree = 3
    learning_rate = 0.01
    trainset, targetset = get_training_n_target_set(sample_num, mu, sigma)
    w = init_w(degree+1)
    get_error(degree, w, trainset[:, :1], trainset)
    update_w(degree, w, trainset[:, :1], trainset)


# trainset[:, 1:]
np.transpose(targetset[:, 1:])

plt.plot(trainset[:, 1:], linewidth=2, color='r')
plt.plot(targetset[:, 1:], linewidth=2, color='b')

trainset[:, 0:-1]


gaussian_noise = np.random.normal(mu, sigma, sample_num)

# sample들의 historgram을 출력한다.
count, bins, ignored = plt.hist(gaussian_noise, 30, normed=True)
# sample들을 이용해서 Gaussian Distribution의 shape을 재구축해서 line으로 그린다.
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
         np.exp(- (bins - mu)**2 / (2 * sigma**2)), linewidth=2, color='r')
plt.show()
