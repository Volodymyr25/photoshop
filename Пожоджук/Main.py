from PIL import Image
from PIL import ImageFilter

with Image.open("Sobaka.jpg") as sobaka:
    print("Розмір", sobaka.size)
    print("Формат", sobaka.format)
    print("Тип", sobaka.mode)
    sobaka.show()