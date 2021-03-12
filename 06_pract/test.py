from PIL import Image
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

im = Image.open('image.jpg')
data = np.array(im.getdata()).reshape([im.height, im.width, 3])
x = np.arange(0, im.width)
X = np.array([x, x**2.0, x**3.0, x**4.0, x**5.0]).transpose()
plt.plot(data[0, :, 0], 'r-')
plt.plot(data[0, :, 1], 'g-')
plt.plot(data[0, :, 2], 'b-')
plt.grid()
plt.show()

y = data[0, :, 0]
lm = linear_model.LinearRegression()
lm.fit(X, y)
predicted = lm.predict(X)
plt.plot(y, 'r-')
plt.plot(predicted, 'b-')
plt.grid()
plt.show()

diff = y - predicted
bits_per_channel = 5
threshold = 2**(bits_per_channel-1)-1
diff = np.clip(diff, -threshold, threshold)
y = predicted + diff
y = np.clip(np.round(y), 0, 255)

pix = im.load()

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
            
for i in range(im.height):
    for j in range(im.width):
        for k in range(3):
            l = list(pix[j, i])
            l[k] = mas[i][k][j]
            pix[j, i] = tuple(l)
im.save('ready_5.jpg')