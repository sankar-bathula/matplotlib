import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('seaborn')

data = pd.read_csv("data_scatter.csv")
view_count=data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count, likes, s=100, c=ratio, cmap='summer', marker='*', 
	edgecolor='black', linewidth=1, alpha=0.75)

cbar = plt.colorbar()
cbar.set_label('Like/Dislike ratio')
#print(likes.head())
plt.xscale('log')
plt.yscale('log')
plt.title("Scatter Plot")
plt.xlabel("View count")
plt.ylabel("Total Likes ")
plt.show()