import matplotlib.pyplot as plt

y = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
N = len(y)
x = range(N)
plt.bar(x, y)


fig = plt.gcf()
plt.show()
