import numpy as np
import math

NOT_FIT = 1         # кандидатка не подходит
FIT = 2             # кандидатка подходит

NUMERICAL = 0       # параметр числовой
CATEGORICAL = 1     # параметр категориальный


def decision_tree(X, Y, scale, level=0):
    # TODO: реализуйте проверку того, что текущий узел необходимо объявить листом
    # и прекратить рекурсию. Условием того, что узел считается листом, является тот
    # факт, что все примеры из Y принадлежат одному классу. Количество классов можно
    # определить с помощью функции np.unique и функции len. Если узел является листом, выведите на экран
    # класс, ассоциированный с этим листом и выйдите из функции (см. код в комментарии ниже).
    # if <узел является листом>:
    #   print('class = %d' % Y[0])
    #   выход из функции
    if len(np.unique(Y)) == 1:
        print('class = %d' % Y[0])
        return


    print('')

    n = X.shape[1]  # количество признаков
    m = X.shape[0]  # количество примеров

    # энтропия до разбиения
    info = Info(Y)

    gain = []
    thresholds = np.zeros(n)

    # цикл вычисления информационного выигрыша
    # по каждому столбцу выборки
    for i in range(n):

        if scale[i] == CATEGORICAL:   # категориальный признак

            # TODO: вычислить информационный выигрыш от разбиения исходного множества
            # по i-му категориальному признаку. Информационный выигрыш считается по формуле:
            # 
            # Gain(S) = Info(T) - InfoS(T),
            # где Info(T) - энтропия исходного множества до разбиения (переменная info - она уже посчитана выше начала цикла).
            # InfoS(T) - энтропия после разбиения (переменная info_s).
            # 
            # Вам необходимо вычислить info_s, а затем на основе этого значения и значения
            # энтропии info вычислить информационный выигрыш gain для i-го признака
            # 
            # Формула для вычисления InfoS(T) приведена в методичке.
            # В этой формуле n равно количеству подмножеств, на которое разбивается исходное множество.
            # В случае категориальных переменных - это количество уникальных значений для i-го признака
            # может быть посчитано как len(np.unique(X[:,i]))
            # Для числовых переменных n = 2 (подмножество <= порога, и подмножество > порога)
            #
            # Пример расчёта:
            # Например, если матрица X выглядит так:
            # [1 2 3]
            # [2 5 1]
            # [4 2 7]
            # 
            # |Ti|/|T| - вероятность i-го подмножества в множестве T. Считается как количество элементов
            # в i-м подмножестве, делённое на количество элементов в множестве T.
            # 
            # Info(Ti) - энтропия i-го подмножества. Считается с помощью функции Info, в которую передается подвектор Y, соответствующий i-му подмножеству.
            # 
            # Будьте внимательны при именовании переменных. Переменные n и i уже заняты (n - количество признаков, i - номер признака,
            # для которого считается информационный выигрыш). Соответственно, те n и i, что используются в формуле, вам нужно назвать по-другому.
            # 
            # info_s = 0
            # ... <код для вычисления info_s> ...
            # gain.append(info - info_s)
            #
            info_s = 0
            nn = len(np.unique(X[:,i]))
            values, counts = np.unique(X[:,i], return_counts=True)
            for ii in range(nn):
                info_s += (counts[ii]/m) * Info(Y[X[:,i] == values[ii]])
            gain.append(info - info_s)

        else:  # непрерывный признак
            # сортируем столбец по возрастанию
            val = np.sort(X[:, i])

            local_gain = np.zeros(m - 1)

            # количество порогов на 1 меньше числа примеров
            for j in range(m - 1):
                threshold = val[j]
                less = sum(X[:, i] <= threshold)  # количество значений в столбце, <=, чем порог
                greater = m - less  # количество значений в столбце, >, чем порог

                # вычисляем информативность признака при данном пороге
                info_s = (less / m) * Info(Y[X[:, i] <= threshold]) + (greater / m) * Info(Y[X[:, i] > threshold])

                local_gain[j] = info - info_s

            gain.append(np.max(local_gain, axis=0))
            idx = np.argmax(local_gain, axis=0)

            thresholds[i] = val[idx]

    # теперь нужно выбрать столбец с максимальным приростом информации
    max_idx = np.argmax(gain)

    if scale[max_idx] == CATEGORICAL:
        # если этот столбец категориальный
        # запускаем цикл по всем уникальным значениям этого столбца
        categories = np.unique(X[:, max_idx])

        for category in categories:
            # рекурсивно вызываем функцию decision_tree с параметрами:
            sub_x = X[X[:, max_idx] == category, :]
            sub_y = Y[X[:, max_idx] == category]

            print_indent(level)
            print('column %d == %f, ' % (max_idx, category), end='')

            decision_tree(sub_x, sub_y, scale, level + 1)
    else:
        # столбец числовой
        # рекурсивно вызываем decision_tree для значений, меньше порога, и значений, больше порога
        threshold = thresholds[max_idx]

        sub_x = X[X[:, max_idx] <= threshold, :]
        sub_y = Y[X[:, max_idx] <= threshold]

        print_indent(level)
        print('column %d <= %f, ' % (max_idx, threshold), end='')

        decision_tree(sub_x, sub_y, scale, level + 1)

        sub_x = X[X[:, max_idx] > threshold, :]
        sub_y = Y[X[:, max_idx] > threshold]

        print_indent(level)
        print('column %d >  %f, ' % (max_idx, threshold), end='')

        decision_tree(sub_x, sub_y, scale, level + 1)


# вычисление энтропии множества set
def Info(set):
    m = len(set)
    info = 0

    n = len(np.unique(set))
    values, counts = np.unique(set, return_counts=True)
    for i in range(n):
        p = counts[i]/m
        info += p*np.log2(p)
    info = -info
    return info
    
    # TODO: вычислить энтропию множества T, пользуясь формулой информационной энтропии,
    # приведенной в методичке. Для определения количества классов во множестве T
    # (параметр n в формуле) воспользуйтесь функцией np.unique. Условно полагаем, что
    # логарифм (np.log2) от нуля равен нулю. Результат вычисления энтропии должен быть записан
    # в переменную info, которая возвращается из функции.


# печать отступа (дня наглядности)
def print_indent(level):
    print(level * '  ', end='')
