import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("./data/ng_microchips.csv", header=None)
df.head()

df.describe()