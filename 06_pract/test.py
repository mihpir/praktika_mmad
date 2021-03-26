# вариант №2
import sys
from PIL import Image
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

# с помощью класса Image из библиотеки Pillow (PIL) открываем изображение
im = Image.open('image.jpg')
# сохраняем оттенки цветов изображения в 3-мерный массив data
data = np.array(im.getdata()).reshape([im.height, im.width, 3])
# создаем матрицу входных признаков, используя полином 5 степени
x = np.arange(0, im.width)
X = np.array([x, x**2.0, x**3.0, x**4.0, x**5.0]).transpose()
# отображение на графике всех цветовых каналов для первой строки изображения
plt.plot(data[0, :, 0], 'r-')
plt.plot(data[0, :, 1], 'g-')
plt.plot(data[0, :, 2], 'b-')
plt.grid()
plt.show()

# отображение на одном графике реальных (y) и предсказанных (predicted) значений для красного цвета первой строки изображения
y = data[0, :, 0]
lm = linear_model.LinearRegression()
lm.fit(X, y)
predicted = lm.predict(X)
plt.plot(y, 'r-')
plt.plot(predicted, 'b-')
plt.grid()
plt.show()

# вычисление разностей реальных и вычисленных по формуле оттенков
diff = y - predicted
# задаём, сколько бит потребуется для хранения разностей по каждой точке
bits_per_channel = 5
# количество оттенков в разностях, которое можно закодировать данным числом бит
threshold = 2**(bits_per_channel-1)-1
# разности, которые выходят за пределы treshold, должны быть искусственно обрезаны до значений treshold
diff = np.clip(diff, -threshold, threshold)
# получение усеченных реальных значений оттенков
y = predicted + diff
y = np.clip(np.round(y), 0, 255)

# получение измененных значений оттенков всех цветовых каналов для всего изображения
mas = [[0]*3 for i in range(im.height)]
for i in range(im.height):
    for j in range(3):
            y = data[i, :, j]
            lm = linear_model.LinearRegression()
            lm.fit(X, y)
            predicted = lm.predict(X)
            diff = y - predicted
            diff = np.clip(diff, -threshold, threshold)
            y = predicted + diff
            y = np.clip(np.round(y), 0, 255)
            mas[i][j] = y.astype(int)

# подмена пикселов в исходном изображении
pix = im.load()
for i in range(im.height):
    for j in range(im.width):
        for k in range(3):
            l = list(pix[j, i])
            l[k] = mas[i][k][j]
            pix[j, i] = tuple(l)
# сохранение изображения
if len(sys.argv) == 1: print('Передайте имя файла (без расширения) в качестве аргумента командной строки')
else: im.save(sys.argv[1]+'.jpg')
