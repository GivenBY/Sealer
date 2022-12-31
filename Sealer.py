from PIL import Image, ImageDraw, ImageFont

# Enter the image name
image = Image.open('sample.jpg')

width, height = image.size

draw = ImageDraw.Draw(image)

# you can use custom Fonts too by downloading from internet
font = ImageFont.truetype('arial.ttf', 30)
text_color = (255, 255, 255)
ascent, descent = font.getmetrics()

# Enter The text to be used for Water Mark
text_string="WaterMark"

text_width = font.getmask(text_string).getbbox()[2]
text_height = font.getmask(text_string).getbbox()[3] + descent

draw.text(((width-text_width)//2,(height-text_height)//2), text_string, fill=text_color, font=font)

# Save the watermarked image
image.save('output.jpg')
