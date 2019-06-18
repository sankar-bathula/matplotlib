from matplotlib import pyplot as plt
plt.style.use("ggplot")
slices = [59219,55466,47544, 36443, 65917]
labels = ["Python", "Java", "HTML/CSS", "SQL","Javascript"]

#colors = ["#008fd5", "#fc4f30", "#e5ae37","#6d904f"]
explode = [0.1,0,0,0,0]
plt.pie(slices, labels=labels, shadow=True, startangle=90,
		 wedgeprops={'edgecolor':'black'}, autopct="%1.1f%%", explode=explode)
plt.title("My awseome pi chart")
plt.tight_layout()
plt.show()