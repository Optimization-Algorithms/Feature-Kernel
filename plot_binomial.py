#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import os

def fact(n):
    if n == 0:
        return 1

    for i in range(2, n):
        n *= i
    return n


def binomial(n, m):
    num = fact(n)
    den = fact(n - m) * fact(m)
    return num / den

def plot_values(x, y, file_name=None):
    fig = plt.figure()
    ax = plt.gca()
    ax.scatter(x, y, c='blue')
    ax.set_yscale('log')
    plt.tight_layout()
    if file_name:
        file_path = os.path.join("images", file_name)
        plt.savefig(file_path)
    else:
        plt.show()

def binomial_range(n):
    x = np.arange(n + 1)
    y = np.asarray([binomial(n, x) for x in x])
    return (x, y)
    
    
    
    


def main():
    x, y = binomial_range(20)
    plot_values(x, y, "binomial-20.eps")
    y = 1 / y
    plot_values(x, y, "inv-binomial-20.eps")

if __name__ == '__main__':
    main()

