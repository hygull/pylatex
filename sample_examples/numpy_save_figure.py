"""
	{
		"createdOn": "21 Feb 2018",
		"aim": "Saving figure generated using numpy & matplotlib",
		"createdBy": "Rishikesh Agrawani"
	}
"""
import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0, 2*np.pi, 100)
y = np.power(x, 2)

plt.plot(x, y)
plt.savefig("my_numpy_plot.png")
plt.show()
