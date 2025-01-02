import matplotlib.pyplot as plt

# Data
x = [i for i in range(0, 11, 1)]
y = [i ** 2 for i in x]

# Plotting the data
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot of x vs y')
plt.show()
