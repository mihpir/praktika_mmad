#вариант №5
import random
def absDiff(m1, m2):
    if len(m1)!=len(m2): raise Exception("Разные размеры массивов")
    return [abs(m1[i]-m2[i]) for i in range(len(m1))]
try:
    print('Задание 1:\t', absDiff([4,7,9,8], [1,17,2,8]), '\n')
except Exception as e:
    print("Было сгенерировано исключение: " + str(e) + "\n")

def fib(n):
    if n == 1: return [1]
    elif n == 2: return [1, 1]
    else:
        a = fib(n-1)
        return a + [a[-2] + a[-1]]
print('Задание 7:\t', fib(10), '\n')

def minMax(n):
    a = [round(random.uniform(-1000, 1000), 2) for i in range(n)]
    return (min(a), max(a))
print('Задание 10:\t', minMax(10), '\n')
