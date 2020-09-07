#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({
    "text.usetex": True,
    "lines.markersize" : plt.rcParams['lines.markersize'] * 0.8
    })

def grow_function(begin, exp, count):
    output = np.zeros(count)
    for i in range(count):
        output[i] = begin
        begin **= exp
    return output




def main():
    begin = 0.01
    count = 30
    for i in range(2, 6):
        exp = (i-1)/i
        grow = grow_function(begin, exp, count)
        plt.scatter(np.arange(count), grow, marker='o')
        plt.plot(grow)
    
    
    plt.legend([f"$\sqrt[{i}]{{ur^{i-1}}}$" for i in range(2, 6)])
    
    ans = input('Save? [Y/n]')
    if "yes".startswith(ans.lower()):
        plt.savefig("infeasible_grow_plot.eps")
    else:
        plt.show()

    


if __name__ == '__main__':
    main()










