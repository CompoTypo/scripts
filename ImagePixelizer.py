from PIL import Image, ImageFilter
from math import ceil
import sys

if len(sys.argv) != 3:
    print('FORMAT ERR: $ python ImagePixerlizer.py <jpg|png> <pixelDensity>', file=sys.stderr)
    exit()

# Read image
im = Image.open(sys.argv[1])
im.show()

BlockDensity = int(sys.argv[2])  # pixels
x, y = im.size
[num_x_blocks, num_y_blocks] = [ceil(x / BlockDensity), ceil(y / BlockDensity)]
temp_im = im.resize((num_x_blocks * BlockDensity, num_y_blocks * BlockDensity))
px = temp_im.load()

for i in range(num_x_blocks):
    for j in range(num_y_blocks):
        # each large block (new pixel)
        cSum = [0, 0, 0]
        pCount = 0

        for k in range(i*BlockDensity, i*BlockDensity + BlockDensity):
            for l in range(j*BlockDensity, j*BlockDensity + BlockDensity):
                # for each pixel in each block
                for col_i in range(len(cSum)):
                    cSum[col_i] += px[k, l][col_i]

                pCount += 1

        blockColor = (ceil(cSum[0] / pCount),
                      ceil(cSum[1] / pCount),
                      ceil(cSum[2] / pCount))
        for k in range(i*BlockDensity, i*BlockDensity + BlockDensity):
            for l in range(j*BlockDensity, j*BlockDensity + BlockDensity):
                px[k, l] = blockColor
# Display image
temp_im.show()

# Applying a filter to the image
im_sharp = temp_im.filter(ImageFilter.SHARPEN)
# Saving the filtered image to a new file
im_sharp.save('image_sharpened.png', 'PNG')

# Viewing EXIF data embedded in image
#exif_data = im._getexif()
# print(exif_data)
