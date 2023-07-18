# from tkinter import Tk, Button
# from PIL import ImageTk, Image
#
#
# class MyButton(Button):
#     def __init__(self, pict, command):
#         self.image = Image.open(pict)
#         self.image = self.image.resize((100, 100))
#         self.pict = ImageTk.PhotoImage(self.image)
#         super().__init__(image=self.pict, command=command)
#
#
# root = Tk()
# root.geometry('800x600')
# root.title('Красная кнопка')
# image = 'slon.jpg'
# pict = ImageTk.PhotoImage(file=image)
# # Button(root, image=pict, command=lambda: print('click')).pack()
#
# MyButton(image, command=lambda: print('click')).pack()
# root.mainloop()
import os
import time
from datetime import datetime


def dish(num, prepare, wait):
    print(f'Начало приготовления блюда {num} - {datetime.now().strftime("%H:%M:%S")}. Приготовление {prepare} мин.')
    time.sleep(prepare)
    print(f'Начало приготовления блюда {num} - {datetime.now().strftime("%H:%M:%S")}. Ожидание {num} {wait} мин.')
    time.sleep(wait)
    print(f'В  {datetime.now().strftime("%H:%M:%S")} блюдо {num} готово.')

t0 = time.time()
dish(1, 2, 3)
dish(2, 5, 10)
dish(3, 3, 5)
delta = int(time.time() - t0)
print(f' в {datetime.now().strftime("%H:%M:%S")} мы закончили')
print(f'Затраченное время {delta}')