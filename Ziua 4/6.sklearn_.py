import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import make_regression

rezultat=make_regression(n_samples=3, n_features =1, n_targets=1)
print(rezultat)