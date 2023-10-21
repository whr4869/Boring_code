from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
# 创建一个新的浏览器实例
driver = webdriver.Chrome(ChromeDriverManager().install())
# 让浏览器打开一个网页
driver.get("https://portal.speexx.cn/login")
# 等待30秒 自己登录
time.sleep(30)
# 视频链接前缀
prefix = "https://portal.speexx.cn/articles/7084920/video/"
# 生成后缀列表
suffixes = [str(i) for i in range(520, 800)]  # 生成520到799的后缀
# 遍历后缀列表并打开视频链接
for suffix in suffixes:
    url = prefix + suffix
    driver.get(url)
    # 查找并点击播放按钮
    play_button = driver.find_element_by_xpath("//button[@title='Play Video']")
    play_button.click()
    # 间隔500秒  
    time.sleep(500)
# 关闭浏览器
driver.quit()



