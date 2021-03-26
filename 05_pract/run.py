import numpy as np
from decision_tree import *

# обучающее множество
X = np.array([
  [110, 1, 1, 2.8],     # FIT
  [95,  2, 1, 2.2],     # FIT
  [135, 1, 1, 2.9],     # FIT
  [115, 1, 0, 2.0],     # FIT
  [100, 2, 0, 2.9],     # NOT_FIT
  [90,  1, 0, 3.5],     # FIT
  [75,  1, 1, 3.1],     # FIT
  [85,  2, 1, 3.1],     # NOT_FIT
  [65,  0, 1, 2.1],     # NOT_FIT
  [70,  1, 0, 3.0]])    # NOT_FIT

# класс для каждой кандидатки:
Y = np.array([FIT, FIT, FIT, FIT, NOT_FIT, FIT, FIT, NOT_FIT, NOT_FIT, NOT_FIT])

# типы переменных в столбцах обучающей выборки
scale = np.array([NUMERICAL, CATEGORICAL, CATEGORICAL, NUMERICAL])

# рекурсивное построение дерева решений
dt = DecisionTree()
dt.fit(X, Y, scale)

# классификация каждого примера с помощью
# классификатора, созданного на основе дерева
y = np.array([dt.predict(X[i, :]) for i in range(len(X))])

# классификация успешна, если все примеры правильно классифицированы
if np.all(y == Y):
    print('\nclassification success!\n')
else:
    print('\nclassification fail... :(\n')

# проверка себя с помощью классификатора
# TODO: после того, как вы построили дерево решений и реализовали на его
# основе функцию predict, раскомментируйте код ниже и проверьте себя,
# подходите ли вы на роль ассистентки профессора Буковски :)
print('Test yourself!')
iq = int(input('iq: '))
articles = int(input('articles: '))
obr = int(input('obr: '))
ratio = float(input('ratio: '))

if dt.predict(np.array([iq, articles, obr, ratio])) == FIT:
     print('You are passed!')
else:
     print('You are not passed, sorry...')