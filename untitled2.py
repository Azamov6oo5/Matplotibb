# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ITyFLrtErkYZq8DgcDLFKJMv-v0ltGEm
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50) * 10
y = np.random.rand(50) * 10
plt.scatter(x, y)
plt.show()