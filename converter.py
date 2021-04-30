from PIL import Image
import json

inputimg = input("File name(.jpg/.jpeg only): ")
outputname = input("Output file name(without .json): ")

try:
  firstimg = inputimg + ".jpeg"
  img = Image.open(firstimg)
except FileNotFoundError:
  firstimg = inputimg + ".jpg"
  img = Image.open(firstimg)

coords = []

for y in range(img.height):
  for x in range(img.width):
    coords.append(f'{x + 1}x{y + 1}')
    pixel = img.getpixel((x, y))

output = dict.fromkeys(coords)
print("\nPixels loaded!\n")

for y in range(img.height):
  for x in range(img.width):
    pixel = img.getpixel((x, y))
    pixhex = '%02x%02x%02x' % pixel
    finalpix = "#" + str(pixhex)

    output[f'{x + 1}x{y + 1}'] = finalpix

print("Colors loaded!\n")

with open(f'{outputname}.json', 'w') as outfile:
  json.dump(output, outfile)

print("File edited!\n")

print("Done!")


