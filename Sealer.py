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
    zoom_x = 2.0                                                     # horizontal zoom
    zoom_y = 2.0                                                     # vertical zoom
    mat = fitz.Matrix(zoom_x, zoom_y)                                # zoom factor 2 in each dimension
    all_files = glob.glob(file)
    doc = fitz.open(all_files)                                       # open document
    for page in doc:                                                 # iterate through the pages
        pix = page.get_pixmap(matrix=mat)                            # render page to an image
        pix.save("../OutputJpg/page-%i.jpg" % page.number)           # store image as a PNG
        if wmark==("y" or "Y"):
            imgWatermark(("../OutputJpg/page-%i.jpg" % page.number),Watermark)        

def jpg_pdf():
    images = [Image.open(f) for f in os.listdir("../jpg-pdf")]
    pdf_path = "/"
    images[0].save(pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])

while True:
    print('''To add waterMark to Single Jpg File >> W''')
    print('''To Extract Jpg From Pdf File and Add WaterMark >> k''')
    print('''To add waterMark to Single File >> W''')
    k=input("Enter >> ")


jpg_pdf()
pdf_jpg()
imgWatermark()