import cv2
import sys


#where I am at:  Trying to tune this so it works in general without a human needing to tune the parameters of the algorithm to get only the actual human faces.

#The idea is very simple: if a rectangle appears often amongst the possible results from different parameters we conclude there is a face of an actual human in that location.  This does not have a theoretical backing at this point and appears to only be from observation, so it is possibly very wrong.

def face_detect(scale_factor,min_neighbors,minSize_x,minSize_y):
# Get user supplied values
    imagePath = sys.argv[1]
    cascPath = sys.argv[2]

# Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=scale_factor,
        minNeighbors=min_neighbors,
        minSize=(minSize_x, minSize_y),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
        )

    return len(faces),faces,image

def tuning():
    #trying the default values
    num_faces,faces,image = face_detect(1.1,5,30,30)
    
    scale_factors = [1.1,1.2,1.3]
    #min_neighbors = 1
    #minSize_x = 10
    #minSize_y = 10
    collected_faces = []
    for min_neighbor in xrange(1,2):
        for minSize in xrange(10,30,10):
            for scale_factor in scale_factors:
                num_faces,faces,image = face_detect(scale_factor,min_neighbor,minSize,minSize)
                if num_faces > 0:
                    parameters = {}
                    parameters['scale_factor'] = scale_factor
                    parameters['min_neighbors'] = min_neighbor
                    parameters['minSize'] = minSize
                    collected_faces.append([num_faces,faces,image,parameters])
    possible_faces = []
    for collected in collected_faces:
        # print "Found {0} faces!".format(collected[0])
        # print "parameters:"
        # print "scale_factor:",collected[3]['scale_factor']
        # print "min_neighbors:",collected[3]['min_neighbors']
        # print "min_size_x:",collected[3]['minSize']
        # print "min_size_y:",collected[3]['minSize']
        # Draw a rectangle around the faces
        for (x, y, w, h) in collected[1]:
            #cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            coordinates = [x,y,x+w,y+h]
            possible_faces.append(coordinates)
        #cv2.imshow("Faces found", image)
        #cv2.waitKey(2000)
    
    return possible_faces,image

def face_find(potential_faces,epsilon,tolerance_level):
    matches = [0 for x in range(len(potential_faces))]
    for ind,candidate in enumerate(potential_faces):
        for coordinate_set in potential_faces:
            if coordinate_set[0] - epsilon < candidate[0] < coordinate_set[0] + epsilon:
                if coordinate_set[1] - epsilon < candidate[1] < coordinate_set[1] + epsilon:
                    matches[ind] += 1
    faces = []
    for ind,match in enumerate(matches):
        #print match/float(len(matches))
        if match/float(len(matches)) > tolerance_level:
            faces.append(potential_faces[ind])
    return faces

potential_faces,image = tuning()
faces = face_find(potential_faces,5,0.01)

for face in faces:
    cv2.rectangle(image, (face[0],face[1]),(face[2],face[3]), (0,255,0),2)
    cv2.imshow("Faces found", image)
    cv2.waitKey(3000)
