from PIL import Image, ImageDraw, ImageFont
import os

# set up the watermark text and font
watermark_text = "ENOOBIS"
font = ImageFont.truetype("ARIAL.TTF", 36)

# set up the input and output directories
input_dir = "INPUT/"
output_dir = "OUTPUT/"

# create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# iterate over all files in the input directory
for filename in os.listdir(input_dir):
    # check if the file is a JPG or PNG image
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # open the image and create a new image with the same size and format
        with Image.open(input_dir + filename) as img:
            img_watermark = Image.new(img.mode, img.size)
            # draw the original image onto the new image
            img_watermark.paste(img, (0, 0))
            # draw the watermark text onto the new image
            draw = ImageDraw.Draw(img_watermark)
            text_width, text_height = draw.textsize(watermark_text, font)
            x = img.size[0] - text_width - 10
            y = img.size[1] - text_height - 10
            draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))
            # save the new image with the watermark
            img_watermark.save(output_dir + filename)