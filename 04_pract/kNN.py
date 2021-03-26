import numpy as np
import math

class KNN:
    
    # Метод fit принимает обучающую выборку как матрицу признаков X
    # и вектор классов y, сохраняет нормализованную выборку
    # и параметры нормализации.
    def fit(self, sub_X, y):
        self.means = np.mean(sub_X, axis=0)
        self.stds = np.std(sub_X, axis=0)
        self.sub_X = (sub_X - self.means) / self.stds
        self.y = y
        
    # Метод predict принимает объект, выполняет его нормализацию
    # с сохранёнными ранее параметрами нормализации и выдаёт класс объекта.
    def predict(self, obj, k):
        obj = (obj - self.means) / self.stds
        d = [dist(obj, self.sub_X[i,:]) for i in range(self.sub_X.shape[0])]
        d_sort = np.argsort(d)
        nearest_classes = self.y[d_sort[0:k]]
        unique, counts = np.unique(nearest_classes, return_counts=True)
        object_class = unique[np.argmax(counts)]
        return object_class
    
# вычисление евклидова расстояния между двумя точками
def dist(p1, p2):
    return math.sqrt(sum((p1 - p2)**2))