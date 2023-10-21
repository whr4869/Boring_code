import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import pandas as pd

def create_2color_images(filename):
    df = pd.read_csv(filename, names=['color1', 'color2'])

    for index, row in df.iterrows():
        fig, ax = plt.subplots()

        circle1 = Circle((0, 0), 1, color=row['color1'], alpha=0.5)
        circle2 = Circle((1.5, 0), 1, color=row['color2'], alpha=0.5)

        ax.add_patch(circle1)
        ax.add_patch(circle2)

        ax.set_xlim(-1.3, 2.7)
        ax.set_ylim(-2, 2)

        plt.gca().set_aspect('equal', adjustable='box')
        plt.axis('off')  # 关闭坐标轴

        # 添加颜色标签
        plt.text(-0.5, -1.5, row['color1'], ha='center')
        plt.text(2, -1.5, row['color2'], ha='center')

        # 为每个图像指定一个唯一的文件名
        plt.savefig('image_{}.png'.format(index))

        plt.close()  # 关闭图像，以节省内存

def create_3color_images(filename):
    df = pd.read_csv(filename, names=['color1', 'color2', 'color3'])

    for index, row in df.iterrows():
        fig, ax = plt.subplots()

        circle1 = Circle((0, 0), 1, color=row['color1'], alpha=0.5)
        circle2 = Circle((1.5, 0), 1, color=row['color2'], alpha=0.5)
        circle3 = Circle((0.75, 0.75), 1, color=row['color3'], alpha=0.5)

        ax.add_patch(circle1)
        ax.add_patch(circle2)
        ax.add_patch(circle3)

        ax.set_xlim(-1.3, 2.7)
        ax.set_ylim(-2, 2)

        plt.gca().set_aspect('equal', adjustable='box')
        plt.axis('off')  # 关闭坐标轴

        # 添加颜色标签
        plt.text(-0.5, -1.5, row['color1'], ha='center')
        plt.text(2, -1.5, row['color2'], ha='center')
        plt.text(0.75, -1.5, row['color3'], ha='center')

        # 为每个图像指定一个唯一的文件名
        plt.savefig('image_{}.png'.format(index))

        plt.close()  # 关闭图像，以节省内存


#输入色卡盘的数量
number=input()

if number=='2':
    create_2color_images('colors.csv')
    pass
elif number=='3':
    create_3color_images('colors.csv')
    pass
elif number=='4':
    create_4color_images('colors.csv')
    pass
elif number=='5':
    create_5color_images('colors.csv')
    pass
else:
    print('有问题哦')
    pass






