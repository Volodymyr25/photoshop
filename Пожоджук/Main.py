from PIL import Image
from PIL import ImageFilter

with Image.open("Sobaka.jpg") as sobaka:
    print("Розмір", sobaka.size)
    print("Формат", sobaka.format)
    print("Тип", sobaka.mode)
    sobaka.show()


    sobaka_gray = sobaka.convert("L")
    sobaka_gray.save("gray.jpg")
    print("Розмір", sobaka_gray.size)
    print("Формат", sobaka_gray.format)
    print("Тип", sobaka_gray.mode)

    pic_blured = sobaka.filter(ImageFilter.BLUR)
    pic_blured.save('blured.jpg')
    pic_blured.show()

    pic_up = sobaka.transpose(Image.ROTATE_180)
    pic_up.save("up.jpg")
    pic_up.show()

    sobaka_gray.show()
