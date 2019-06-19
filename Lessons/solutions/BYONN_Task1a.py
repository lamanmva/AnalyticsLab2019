#Task 1a: What is the first derivative of the sigmoid function?
# Plot this function

import matplotlib.pyplot as plt
x = numpy.linspace(-6, 6, 121)
y = scipy.special.expit(x)
plt.plot(x, y*(1-y))
plt.grid()
plt.xlim(-6, 6)
plt.xlabel('x')
plt.title('1st deriv, sigmoid(x)')
plt.show()
