from PIL import Image

catIm = Image.open('zophie.png')

# left, top, right -1, bottom -1`
croppedIm = catIm.crop((335, 345, 565, 560))
croppedIm.save('cropped.png')