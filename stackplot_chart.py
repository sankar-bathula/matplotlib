from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")
minutes = [1,2,3,4,5,6,7,8,9]
player1 = [1,2,3,3,4,4,4,4,5]
player2 = [1,1,1,1,2,2,2,3,4]
player3 = [1,1,1,1,2,2,2,3,3]

labels = ["player1","player2","player3"]
colors = ["#008fd5","#fc4f30","#6d904d"]
plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)
plt.title("Stack Plot ")
plt.legend(loc="upper left")
#plt.legend(loc=(0.07, 0.05))
plt.tight_layout()
plt.show()
