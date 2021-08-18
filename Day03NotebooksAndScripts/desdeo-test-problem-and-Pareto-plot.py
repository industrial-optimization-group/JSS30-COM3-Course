# # Basics of desdeo-emo
import matplotlib.pyplot as plt

import plotly.graph_objects as go
import numpy as np
import pandas as pd

from desdeo_problem import variable_builder, ScalarObjective, MOProblem
from desdeo_problem.testproblems.TestProblems import test_problem_builder

from desdeo_emo.EAs import NSGAIII


# ## Coello MOP7
#
# ### Definition
# ![Definition](https://raw.githubusercontent.com/industrial-optimization-group/desdeo-emo/master/docs/notebooks/notebook_extras/MOP7.png)
#
# ### Pareto set and front
# ![Front](https://raw.githubusercontent.com/industrial-optimization-group/desdeo-emo/master/docs/notebooks/notebook_extras/MOP7_PF.png)

# Coello, Carlos A. Coello, Gary B. Lamont, and David A. Van Veldhuizen. Evolutionary algorithms for solving multi-objective problems. Vol. 5. New York: Springer, 2007.

# ## Define objective functions



def f_1(x):
    term1 = ((x[:,0] - 2) ** 2) / 2
    term2 = ((x[:,1] + 1) ** 2) / 13
    return term1 + term2 + 3

def f_2(x):
    term1 = ((x[:, 0] + x[:, 1] - 3) ** 2) / 36
    term2 = ((-x[:, 0] + x[:, 1] + 2) ** 2) / 8
    return term1 + term2 - 17

#def f_3(x):
#    term1 = ((x[:, 0] + (2 * x[:, 1]) - 1) ** 2) / 175
#    term2 = ((-x[:, 0] + 2* x[:, 1]) ** 2) / 17
#    return term1 + term2 - 13


# Note that the expected input `x` is two dimensional. It should be a 2-D numpy array.

# ## Create Variable objects

# [lower bound x1, lower bound x2], [upper  bound x1, upper bound x2]
list_vars = variable_builder(['x', 'y'],
                             initial_values = [0,0],
                             lower_bounds=[0, 0],
                             upper_bounds=[10, 5])
list_vars


# ## Create Objective objects


f1 = ScalarObjective(name='f1', evaluator=f_1)
f2 = ScalarObjective(name='f2', evaluator=f_2)
list_objs = [f1, f2]


# ## Create the problem object


problem = MOProblem(variables=list_vars, objectives=list_objs)


# ## Using the EAs
#
# Pass the problem object to the EA, pass parameters as arguments if required.


evolver = NSGAIII(problem,
                  n_iterations=10,
                  n_gen_per_iter=100,
                  population_size=100)


while evolver.continue_evolution():
    evolver.iterate()


# ## Visualization of optimized decision variables and objective values using Plotly

# individuals: decision variable vectors
# solutions: points in objective space that approximate Parto front
individuals, solutions = evolver.end()

#fig1 = go.Figure(
#    data=go.Scatter(
#        x=individuals[:,0],
#        y=individuals[:,1],
#        mode="markers"))
#fig1


#fig2 = go.Figure(data=go.Scatter3d(x=solutions[:,0],
#                                   y=solutions[:,1],
#                                   z=solutions[:,2],
#                                   mode="markers",
#                                   marker_size=5))
#fig2


#pd.DataFrame(solutions).to_csv("MOP7_true_front.csv")
# pip install matplotlib (in terminal)
# import matplotlib.pyplot as plt
plt.scatter(solutions[:,0],solutions[:,1])
plt.show()