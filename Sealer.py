import img2pdf
import glob,fitz
import os
from PIL import Image, ImageDraw, ImageFont

# Enter the image name
def imgWatermark(file,Watermark):
    image = Image.open(file)
    width, height = image.size
    draw = ImageDraw.Draw(image)

    # you can use custom Fonts too by downloading from internet
    font = ImageFont.truetype('arial.ttf', 30)
    text_color = (255, 255, 255)
    ascent, descent = font.getmetrics()

    # Enter The text to be used for Water Mark
    text_string=Watermark
    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent
    draw.text(((width-text_width)//2,(height-text_height)//2), text_string, fill=text_color, font=font)

    # Save the watermarked image
    image.save('output.jpg')

def pdf_jpg(file,wmark,Watermark):
    pass

def jpg_pdf():
    with open("123.pdf","wb") as f:
        f.write(img2pdf.convert(glob.glob(os.getcwd()+"/Images/*.jpg")))

while True:
    print('''To add waterMark to Single Jpg File >> W/w''')
    print('''To Extract Jpg From Pdf File and Add WaterMark >> J/j''')
    print('''To Extract Pdf File From Images *Put all Images in Images folder* >> A/a''')
    print('''Press Another Key to Escape >>''')
    k=input("Enter >> ")
    if k=="W" or k=="w":
        file=input("Enter File Name : ")
        watmark=input("Enter WaterMark")
        imgWatermark(file,watmark)
    elif k=="J" or k=="j":
        print('''Do you want to add add WaterMark >>''')
        print('''Press y/y for Yes else any key for No''')
        c=input("Input Choice : ")
        if c=="y" or c=="Y":
            file=input("Enter File Name : ")
            watmark=input("Enter WaterMark")
            pdf_jpg(file,watmark,c)
        else:
            file=input("Enter File Name : ")
            watmark=input("Enter WaterMark")
            pdf_jpg(file,watmark,"No")
    elif k=="A" or k=="a":
        jpg_pdf()
    else:
        break