# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from PIL import Image, ImageFilter

img = Image.open('./sample_Images/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(dir(img))
    filtered_img.save("blur.png", "png")
    filtered_img.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
