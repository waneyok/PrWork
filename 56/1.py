print('Code 1')
import matplotlib.pyplot as plt
data = [10, 15, 20, 22, 30, 36, 45, 50]
plt.hist(data, bins=5)
plt.show()

print('Code 2')
import matplotlib.pyplot as plt
x = [10, 15, 20, 22, 30, 36, 45, 50]
y = [100, 120, 140, 150, 180, 200, 210, 235]
plt.scatter(x, y)
plt.show()

print('Code 3')
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 22, 30]
plt.plot(x, y)
plt.show()

print('Code 4')
import matplotlib.pyplot as plt
labels = ['Категория 1', 'Категория 2', 'Категория 3']
sizes = [50, 25, 25]
colors = ['yellowgreen', 'gold', 'lightskyblue']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.show()
