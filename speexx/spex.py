from tkinter import *
from PIL import Image, ImageTk
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def create_window():
    window = Tk()
    window.title("My Window")
    # 添加图片
    image = Image.open("C:/Users/wangh/Desktop/spex/c5030c9dd6168cc7d04b49a7d246fa7.jpg")
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
        start_selenium()

    Button(window, text="点击", command=on_click).pack()

    window.mainloop()

def start_selenium():
    # 创建一个新的浏览器实例
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # 让浏览器打开一个网页
    driver.get("https://portal.speexx.cn/login")

    # 等待30秒
    time.sleep(30)

    # 视频链接前缀
    prefix = "https://portal.speexx.cn/articles/7084920/video/"

    # 生成后缀列表
    suffixes = [str(i) for i in range(520, 800)]  # 生成780到799的后缀

    # 遍历后缀列表并打开视频链接
    for suffix in suffixes:
        url = prefix + suffix
        driver.get(url)
        # 查找并点击播放按钮
        play_button = driver.find_element_by_xpath("//button[@title='Play Video']")
        play_button.click()
        # 间隔5分钟  
        time.sleep(500)

    # 关闭浏览器
    driver.quit()

create_window()
