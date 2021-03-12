import numpy as np
import matplotlib.pyplot as plt
from k_means import kmeans

# исходные данные
X = np.array([
  [4, 4],
  [3, 3],
  [5, 3],
  [2, 3],
  [5, 5],
  [3, 2],
  [2, 4],
  [4, 5],
  [5, 4],
  [2, 2]])

# запуск кластеризации
ans = kmeans(2, X)

# отображение результатов
print(ans)
plt.plot(X[:,0], X[:,1], 'bx', ans[:,0], ans[:,1], 'r*', markersize=20)
plt.grid()
plt.show()
