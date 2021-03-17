NOT_FIT = 1         # кандидатка не подходит
FIT = 2             # кандидатка подходит

def classify(X):
    answer = 0
    iq_level, articles_count, has_education, ratio = X

    # TODO: пользуясь информацией, выведенной на экран в процессе построения
    # дерева решений, запрограммируте классификатор, реализующий логику
    # дерева решений. Используйте для этого простые конструкции if-elif-else, а так же
    # конструкции if-elif-else, вложенные одна в другую там, где это необходимо.
    # Пример:
    # if iq_level <= 70:
    #     answer = NOT_FIT
    # else:
    #     ...
    if iq_level <= 70:
        answer = NOT_FIT
    elif articles_count == 1:
        answer = FIT
    elif ratio <= 2.2:
        answer = FIT
    else:
        answer = NOT_FIT

    return answer
