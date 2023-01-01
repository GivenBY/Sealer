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
    # To get better resolution
    zoom_x = 2.0  # horizontal zoom
    zoom_y = 2.0  # vertical zoom
    mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension

    path = '../'
    all_files = glob.glob(path + "*.pdf")

    for filename in all_files:
        doc = fitz.open(filename)  # open document
        for page in doc:  # iterate through the pages
            pix = page.get_pixmap(matrix=mat)  # render page to an image
            pix.save("../OutputJpg/page-%i.png" % page.number)  # store image as a PNG

def jpg_pdf(file):
    images = [Image.open(f) for f in os.listdir(f"../Images/{file}")]
    pdf_path = "/"
    images[0].save(pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])

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
        file=input("Enter File Name : ")
        jpg_pdf(file)
    else:
        break