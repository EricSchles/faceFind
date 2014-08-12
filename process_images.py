from FaceDetect.face_detect import run
import glob
import Image
import os
images = glob.glob("preprocessed/*")

#adding comment for no reason
for image in images:
    png_img = image.split(".")[0] + ".png"
    im = Image.open(image)
    im.save(png_img)
    os.remove(image)
    print png_img
    run(png_img)
