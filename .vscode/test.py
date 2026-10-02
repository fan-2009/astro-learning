import sys
print("当前 Python 路径:", sys.executable)

import astropy, numpy, matplotlib, scipy, pandas
print("Astropy:", astropy.__version__)
print("NumPy:", numpy.__version__)
print("Matplotlib:", matplotlib.__version__)
print("Scipy:", scipy.__version__)
print("Pandas:", pandas.__version__)
print("OK")

# 简单画图测试
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.title("VS Code 配置测试")
plt.show()