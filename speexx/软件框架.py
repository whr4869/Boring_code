from tkinter import *
from PIL import Image, ImageTk

def create_window():
    window = Tk()
    window.title("My Window")

    # 添加图片
    image = Image.open("c5030c9dd6168cc7d04b49a7d246fa7.jpg")
    image = image.resize((200, 200), Image.LANCZOS)  # 改变图片大小为200x200像素
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    label.image = photo
    label.pack()

    # 添加账号输入框
    Label(window, text="账号").pack()
    input1 = Entry(window)
    input1.pack()

    # 添加密码输入框
    Label(window, text="密码").pack()
    input2 = Entry(window)
    input2.pack()

    # 添加按钮和点击后的文字
    def on_click():
        Label(window, text="自己填").pack()

    Button(window, text="点击", command=on_click).pack()

    window.mainloop()

create_window()
