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
        self.draw =  ImageDraw.Draw(self.imagefile)

    def save(self):
        self.imagefile.save(f'icons\\{self.filename}.png')

    def drawletters(self, font=arial, fontsize=80, fontcolor=Green):
        drawfont = ImageFont.truetype(font, fontsize)
        twidth =  self.draw.textlength(self.letters, font=drawfont)
        x = (256-twidth) / 2
        y = (256-fontsize) / 2
        self.draw.text((x,y), self.letters, font=drawfont, fill=fontcolor, anchor="mm")

    def drawborder(self, color=Blue):
        self.draw.rectangle(((5, 5), (250, 250)), outline=color, width=2)
        self.draw.rectangle(((15, 15), (240, 240)), outline=color, width=2)

    def generate(self):
        self.drawborder()
        self.drawletters()
        self.save()

for icon in to_gen:
    Icon(icon).generate()