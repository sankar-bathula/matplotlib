import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")
ages =[18,19,21,25,26,30,32,38,45,55]
bins = [10,20,30,40,50,60]
plt.hist(ages, bins=bins, edgecolor="black", log=True)
median_age=29
color = "#fc4f30"
plt.axvline(median_age, color=color, label="Age median")
plt.legend()
plt.title("Ages responds")
plt.xlabel("Ages")
plt.ylabel("Total Responds")
plt.tight_layout()
plt.show()