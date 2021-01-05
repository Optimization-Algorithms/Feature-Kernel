#! /usr/bin/python

import sys
import os

file_name = sys.argv[1]

def print_min_max(values, msg):
    try:
        min_val = min(values)
        max_val = max(values)
        print( msg, "&" ,f"{min_val:.5}", "&", f"{max_val:.5}", r' \\ \hline')
    except:
        print( msg, "& N.A. & N.A.", r' \\ \hline')


with open(file_name) as file:
    int_feasible = []
    infeasible = []
    lin_feasible = []
    timeout = []
    selector = {
        '0': lin_feasible,
        '1': int_feasible,
        '2': timeout,
        '' : infeasible
    }
    for line in file:
        [ur, status] = line.strip().split(',')
        selector[status].append(ur)


print(
    r"""
    \begin{table}[H]
    \centering
    \begin{tabular}{|l|c|c|}
    \hline
    Status & Minimum & Maximum \\ \hline \hline
    """
)
print_min_max(infeasible, "Inseasible")
print_min_max(lin_feasible, "Linear Feasible")
print_min_max(int_feasible, "Integer Feasible")
print_min_max(timeout, "Timeout")
file_name = os.path.basename(file_name)
name = file_name.replace("-ratio.csv", "").strip()
print(
    r"\end{tabular}\caption{", f"Statistics about {name}", "}",
    f"\\label{{tab:stats-{name}}}",
    r'\end{table}'
    
)


