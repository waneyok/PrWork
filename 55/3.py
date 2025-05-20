import matplotlib.pyplot as plt

sales = [75, 15, 5, 5]
labels = ['Продукты', 'Одежда', 'Электроника', 'Другое']
plt.pie(sales, labels=labels, autopct='%1.1f%%')
plt.show()
