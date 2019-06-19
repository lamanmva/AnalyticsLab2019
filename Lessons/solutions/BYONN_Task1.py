#Task 1: plot the sigmoid function expit()

import matplotlib.pyplot as plt
x = numpy.linspace(-6, 6, 121)
y = scipy.special.expit(x)
plt.plot(x, y)
plt.grid()
plt.xlim(-6, 6)
plt.xlabel('x')
plt.title('sigmoid(x)')
plt.show()
