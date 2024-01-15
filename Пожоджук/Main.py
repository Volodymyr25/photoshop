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
    sobaka_gray.show()
