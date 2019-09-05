import pandas as pd
from matplotlib import pyplot

data = pd.read_csv('weights2.csv')
arr = []
sums = [0, 0]
for i in data.values:
    arr.append(float(i[2])/float(i[1]))
    sums[0] += float(i[1])
    sums[1] += float(i[2])

print(sums)
values = [1 - (sums[1]/sums[0]), (sums[1]/sums[0])]
labels = [f'code ({round(values[0]*100)}%,\n {int(sums[0]):,} characters)', f'comment ({round(values[1]*100)}%,\n {int(sums[1]):,} characters)']
explode = (0.12, -0.12)
colors = ['#66b3ff', '#99ff99']
fig1, ax = pyplot.subplots()
ax.pie(values, explode=explode, colors=colors, labels=labels, startangle=90)
ax.axis('equal')
ax.set_title('Code and comment weight in Linux Kernel 5.1.14 source code \n (26,939 C files)')
pyplot.tight_layout()

circle = pyplot.Circle((0,0), 0.70, fc='white')
fig = pyplot.gcf()
fig.gca().add_artist(circle)
pyplot.show()
