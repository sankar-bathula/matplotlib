from matplotlib import pyplot as plt
#plt.style.use("ggplot")
#method for stlye of plot
plt.xkcd()
age_x = [26,27,28,29,30,31,32,33,34,35]

#python develpoer data
py_dev_y = [45372, 48876, 53850, 57287, 63016,65998,70003, 70000,71496, 75370]
plt.plot(age_x, py_dev_y, color ='b', marker ='o', linewidth=3, label = "Python")

#Javascript develpoer data
js_dev_y =[37810,43515,46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746]
plt.plot(age_x, js_dev_y, color='#adad3b', marker='*', linewidth=3, label="Javascript")

dev_y = [38496,42000, 46752,49320,53200, 56000, 62316, 64928,67317, 68748]
plt.plot(age_x, dev_y, color ='k', linestyle='--', marker ='.', label="All Devs")

plt.xlabel("Ages")
plt.ylabel("Median of salaries (USD)")
plt.title("Median of salaries (USD) by Ages")
plt.legend()
plt.grid(True) # to show the grid view
plt.show()
plt.savefig("plot.png")