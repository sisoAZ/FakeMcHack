from PIL import Image, ImageDraw, ImageFont
import os

def margeGui(file, overlayFile):
    image = Image.open(file)
    overlayImage = Image.open(overlayFile)

    base = Image.new('RGBA', overlayImage.size, (255, 255, 255, 0))
    resize_image = image.resize(size=(854, 480))
    base.paste(resize_image, (0, 0))
    base.paste(overlayImage, (0, 0), overlayImage)

    filename = os.path.splitext(file)[0]
    base.save(filename + "_fakehack.png")
    return filename + "_fakehack.png"

#margeGui("./1.png", "./hackgui/other.png")