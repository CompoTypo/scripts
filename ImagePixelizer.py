from PIL import Image, ImageFilter
from math import ceil
# Read image
im = Image.open('FB_IMG.png')
im.show()

BlockDensity = 6  # pixels
x, y = im.size
num_x_blocks = ceil(x / BlockDensity)
num_y_blocks = ceil(y / BlockDensity)
temp_im = im.resize((num_x_blocks * BlockDensity, num_y_blocks * BlockDensity))
px = temp_im.load()

for i in range(num_x_blocks):
    for j in range(num_y_blocks):
        # each large block (new pixel)

        colorSum = [0, 0, 0]
        pixelCounter = 0
        for k in range(i*BlockDensity, i*BlockDensity + BlockDensity):
            for l in range(j*BlockDensity, j*BlockDensity + BlockDensity):
                # for each pixel in each block
                for col_i in range(len(colorSum)):
                    colorSum[col_i] += px[k, l][col_i]
                 
                print(colorSum)
                pixelCounter += 1

        blockColorR = ceil(colorSum[0] / pixelCounter)
        blockColorG = ceil(colorSum[1] / pixelCounter)
        blockColorB = ceil(colorSum[2] / pixelCounter)
        blockColor = (blockColorR,blockColorG,blockColorB)
        for k in range(i*BlockDensity, i*BlockDensity + BlockDensity):
            for l in range(j*BlockDensity, j*BlockDensity + BlockDensity):
                px[k,l] = blockColor
# Display image
temp_im.show()

# Applying a filter to the image
im_sharp = temp_im.filter(ImageFilter.SHARPEN)
# Saving the filtered image to a new file
im_sharp.save('image_sharpened.png', 'PNG')

# Viewing EXIF data embedded in image
#exif_data = im._getexif()
#print(exif_data)
