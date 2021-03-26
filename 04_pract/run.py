import numpy as np
from kNN import KNN

# X - обучающее множество
X = np.array([
  [33, 21, 1],
  [41, 13, 1],
  [18, 22, 1],
  [38, 34, 1],
  [62, 118, 2],
  [59, 137, 2],
  [95, 131, 2],
  [83, 110, 2],
  [185, 155, 3],
  [193, 129, 3],
  [164, 135, 3],
  [205, 131, 3],
  [145, 55, 4],
  [168, 35, 4],
  [135, 47, 4],
  [138, 66, 4]]).astype(np.float64)

# ввод роста и веса особи, которую нужно классифицировать
height = int(input('Введите рост особи: '))
weight = int(input('Введите вес особи: '))

obj = np.array([height, weight]).astype(np.float64)

# классификация методом k ближайших соседей
k = 3
cl = KNN()
cl.fit(X[:, 0:-1], X[:, -1])
object_class = cl.predict(obj, k)

# вывод результата классификации
monkeys = {1: 'lemur', 2: 'schimpanze', 3: 'gorilla', 4: 'orangutan'}
print('/nРезультат классификации: ', monkeys[object_class])