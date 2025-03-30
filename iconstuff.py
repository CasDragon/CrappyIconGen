from PIL import Image, ImageDraw, ImageFont

to_gen = [
    "AutoSolidShadows",
    "AutoRime",
    "AutoFlare",
    "AutoEncourage",
    "AutoBurning"
]

Blue = (0, 0, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Yellow = (255, 255, 0)
White = (255, 255, 255)
Black = (0, 0, 0)

arial = "arial.ttf"


class Icon:

    def __init__(self, filename, color=Black):
        self.filename = filename
        self.imagefile = Image.new("RGB", (256, 256), color)
        self.letters = ''.join(ch for ch in self.filename if ch.isupper())
        self.draw = draw = ImageDraw.Draw(self.imagefile)

    def save(self):
        self.imagefile.save(f'icons\\{self.filename}.png')

    def drawletters(self, font=arial, fontsize=80, fontcolor=Green):
        drawfont = ImageFont.truetype(font, fontsize)
        match len(self.letters):
            case 1:
                self.draw.text((95, 80), self.letters, font=drawfont, fill=fontcolor)
            case 2:
                self.draw.text((75, 80), self.letters, font=drawfont, fill=fontcolor)
            case 3:
                self.draw.text((50, 80), self.letters, font=drawfont, fill=fontcolor)
            case _:
                self.draw.text((30, 80), self.letters, font=drawfont, fill=fontcolor)

    def drawborder(self, color=Blue):
        self.draw.rectangle(((5, 5), (250, 250)), outline=color, width=2)
        self.draw.rectangle(((15, 15), (240, 240)), outline=color, width=2)

    def generate(self):
        self.drawborder()
        self.drawletters()
        self.save()

for icon in to_gen:
    Icon(icon).generate()