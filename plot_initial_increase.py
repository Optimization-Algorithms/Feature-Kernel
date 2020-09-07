#! /usr/bin/python

import os
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update(
    {"text.usetex": True, "lines.markersize": plt.rcParams["lines.markersize"] * 0.8}
)


def grow_function(begin, exp, count):
    output = np.zeros(count)
    for i in range(count):
        output[i] = begin
        begin **= exp
    return output


def create_if_missing(dir_path):
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)


def save_figure(base_dir, file_name):
    create_if_missing(base_dir)
    file_name = os.path.join(base_dir, file_name)
    plt.savefig(file_name)


def main():

    begin = 0.01
    count = 30
    for i in range(2, 6):
        exp = (i - 1) / i
        grow = grow_function(begin, exp, count)
        plt.scatter(np.arange(count), grow, marker="o")
        plt.plot(grow)

    plt.legend([f"$\sqrt[{i}]{{ur^{i-1}}}$" for i in range(2, 6)])

    save_figure("images", "plot_initial_increase.eps")


if __name__ == "__main__":
    main()

