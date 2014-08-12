import cv2
import sys
import os
import Image
#convert_rgb_to_bgr expects an image as input, results a grey scale image
#normalize_image_for_face_detection expects an image, returns a resized image
from helper import convert_rgb_to_bgr,normalize_image_for_face_detection
#TODO: Make use of helper function for higher results

# Get user supplied values
#imagePath = sys.argv[1]
#cascPath = sys.argv[2]

def run(imagePath):
# Create the haar cascadels
    cascPath = "FaceDetect/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    
# Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    scaling = [1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2]
    neighbors = [1,2,3]
# Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=1,
        minSize=(20, 20),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
        )

    if len(faces) != 1:
        for scale in scaling:
            for min_size in xrange(10,100,10):
                for neighbor in neighbors:
                    faces = faceCascade.detectMultiScale(
                        gray,
                        scaleFactor=scale,
                        minNeighbors=neighbor,
                        minSize=(min_size, min_size),
                        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
                        )
                    for (x, y, w, h) in faces:
                        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

                    cv2.imshow("Faces found", image)
                    cv2.waitKey(20)
                    
                    if 2 > len(faces) > 0:
                        break
                
    
    if len(faces) == 1:
        
        i = Image.open(imagePath)
        new_image = imagePath.split("/")[1]
        os.chdir("withFace")
        i.save(new_image)
        os.chdir("../")
        print imagePath," this file should be removed"
        os.remove(imagePath)

    print "Found {0} faces!".format(len(faces))

## Draw a rectangle around the faces
    
