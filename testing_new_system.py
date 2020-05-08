import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()

x = np.random.random(30)
y  = x ** 2

plt.scatter(x, y)
plt.title('Testing Stuff')
plt.xlabel("Random X's")
plt.ylabel("Squared Random")
plt.show()