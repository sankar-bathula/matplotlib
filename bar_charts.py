import numpy as np
from matplotlib import pyplot as plt


age_x = [26,27,28,29,30,31,32,33,34,35]
index_x = np.arange(len(age_x))
width =0.25
#python dev data
py_dev_y = [45372, 48876, 53850, 57287, 63016,65998,70003, 70000,71496, 75370]
plt.bar(index_x, py_dev_y, color ='b', width=width, label = "Python")

#Javascript dev data
js_dev_y =[37810,43515,46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746]
plt.bar(index_x+width, js_dev_y, color='#adad3b', width=width, label="Javascript")

dev_y = [38496,42000, 46752,49320,53200, 56000, 62316, 64928,67317, 68748]
plt.bar(index_x-width, dev_y, color ='k', linestyle='--', width=width, label="All Devs")

plt.xlabel("Ages")
plt.ylabel("Median of salaries (USD)")
plt.title("Median of salaries (USD) by Ages")
plt.legend()
plt.grid(True) # to show the grid view
plt.show()
plt.savefig("plot.png")