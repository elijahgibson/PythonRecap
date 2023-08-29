import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))

plt.show()

## not running, we need create a VE (bottom right), activate it (the green letters), install (in this case matplotlib, squiggly lines will disappear)
## don't need to track the VE, gitignore "NAME/"
## students don't submit latest version if it is not checked in, if files in source control, make sure to committ them
## put in name of folder in gitignore with a backslash, then save it,
## then source control, write a message and committ it