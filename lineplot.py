import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv('data.csv')
ages  =data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']
overall_median = 57287
plt.plot(ages, dev_salaries, color="#44444444", linestyle='--', label="All Devs")
plt.plot(ages, py_salaries, label="Python")
plt.plot(ages, js_salaries, label="JavaScript")
plt.legend()
plt.fill_between(ages, py_salaries, overall_median, where=(py_salaries>overall_median), 
					interpolate=True, alpha=0.25)

plt.fill_between(ages, py_salaries, overall_median, 
	where=(py_salaries<=overall_median), color="red",interpolate=True, alpha=0.25)

plt.title("Median Salary (USD) by age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD) ")
plt.show()