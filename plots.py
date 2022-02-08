import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

corr = res.corr()
#corr.style.background_gradient(cmap='coolwarm')
figure = plt.figure(figsize=(20, 10))
ax = sns.heatmap(corr, annot=True)
