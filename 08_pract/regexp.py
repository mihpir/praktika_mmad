import re

def rex(mas, reg):
    for i in mas:
        result = re.search(reg, i)
        if result != None: print(i, ' yes')
        else: print(i, ' no')
    print()

# 2 задание
mas = ['a@b.c', 'a-b@c.d.e', 'a-b_c.d@e_f-g.h', 'a+@b.c', 'a_b.c', 'a_b@.c-d']
reg = r'^[\w\-.]+@[A-Za-z0-9][\w\-]*.[\w\-.]+$'
rex(mas, reg)

# 9 задание
mas = ['123456', '123 456', 'str123456str', '123a456b']
reg = r'^\d{6}$'
rex(mas, reg)

# 10 задание
mas = ['test.png', 'test.jpeg', 'test.jpg', 'test.gif', 'test.php', 'test.exe', '~!@$%.png', '<?php test.png ?>']
reg = r'^[A-Za-z]+\.(png|jpg|jpeg|gif)$'
rex(mas, reg)