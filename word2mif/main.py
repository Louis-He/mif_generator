from PIL import Image, ImageDraw, ImageFont
import math

def changeToTargetBits(r, g, b, bits):
    factor = pow(2, 8) / pow(2, bits)
    return int(math.floor(r/factor)), int(math.floor(g/factor)), int(math.floor(b/factor)), int(factor)

def convertToEightBits(color, bit):
    return int(255 / (pow(2, bit) - 1) * color)

if __name__ == '__main__':
    text = input("Enter Text: ")
    try:
        fontsize = int(input("Font Size(pixel, int): "))
    except ValueError:
        print("Not an integer")
        exit(1)
    try:
        bits = int(input("bits(up to 8, int): "))
    except ValueError:
        print("Not an integer")
        exit(1)
    img = Image.new('RGB', (int(len(text) * fontsize * 0.45), fontsize), color=(255, 255, 255))

    font = ImageFont.truetype(font="Arial.ttf", size=fontsize)
    d = ImageDraw.Draw(img)
    d.text((0, -fontsize * 0.12), text, fill=(0, 255, 0), font=font)

    img.save('out.png')
    imgConverted = img.load()
    imgConvertedOut = Image.new("RGB", (int(len(text) * fontsize * 0.45), fontsize), color=(255, 255, 255))

    length, height = img.size
    mifArray = [[0 for i in range(length)] for j in range(height)]
    for x in range(length):
        for y in range(height):
            r_, g_, b_ = img.getpixel((x, y))
            r, g, b, factor = changeToTargetBits(r_, g_, b_, bits)
            mifArray[y][x] = [r, g, b]

            imgConvertedOut.putpixel((x, y), (convertToEightBits(r, bits), convertToEightBits(g, bits), convertToEightBits(b, bits)))

    imgConvertedOut.save('outConvert.png')

    with open('out.mif', 'w+') as f:
        f.write("-- Created with word2mif file converter\n")
        f.write("-- @ Louis-He\n-- Open-source Project: https://github.com/Louis-He/mif_generator\n\n")
        f.write("WIDTH=" + str(bits) + ";\n")
        f.write("DEPTH=" + str(length * height) + ";\n\n")
        f.write("Address_radix=hex;\nData_radix=bin;\nContent\nBEGIN\n")

        rowStart = 0
        rowIdx = 0
        for row in mifArray:
            f.write('\t\t' + "{0:x}".format(rowStart) + ":\t\t")
            for col in mifArray[rowIdx]:
                r, g, b = col
                singleAddressBits = "{0:b}".format(r).zfill(bits) + "{0:b}".format(g).zfill(bits) + "{0:b}".format(b).zfill(bits)
                f.write(' ' + singleAddressBits)
            f.write(';\n')

            rowStart += length
            rowIdx += 1

        f.write("END;\n")