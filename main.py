from tkinter import Tk, Button
from PIL import ImageTk, Image


class MyButton(Button):
    def __init__(self, pict, command):
        self.image = Image.open(pict)
        self.image = self.image.resize((100, 100))
        self.pict = ImageTk.PhotoImage(self.image)
        super().__init__(image=self.pict, command=command)


root = Tk()
root.geometry('800x600')
root.title('Красная кнопка')
image = 'slon.jpg'
pict = ImageTk.PhotoImage(file=image)
# Button(root, image=pict, command=lambda: print('click')).pack()

MyButton(image, command=lambda: print('click')).pack()
root.mainloop()