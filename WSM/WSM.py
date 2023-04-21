import numpy as np
import pandas as pd
from decipy import executors as exe

# define matrix
matrix = np.array([
    [5, 8, 4],
    [7, 6, 8],
    [8, 8, 6],
    [7, 4, 6]
])

# alternatives
alts = ['A1', 'A2', 'A3', 'A4']

# criterias
crits = ['C1', 'C2', 'C3']

# criteria's beneficial values, True for benefit or False for cost
beneficial = [True, True, True]

# criteria's weights
weights = [0.30, 0.40, 0.30]

# define DataFrame
xij = pd.DataFrame(matrix, index=alts, columns=crits)

# create Executor (MCDM Method implementation)

kwargs = {
    'data': xij,
    'beneficial': beneficial,
    'weights': weights,
    'rank_reverse': True,
    'rank_method': "ordinal"
}

# Build MCDM Executor
wsm = exe.WSM(**kwargs) # Weighted Sum Method

# show results
print("WSM Ranks")
print(wsm.dataframe)

