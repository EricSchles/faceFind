#Intro

faceFind is a very simple tool that makes use of openCV to discover faces in pictures.  It expects a set of pictures in the preprocessed directory.  All output faces will be stored in the withFace directory.

#dependencies

If you are using ubuntu, getting openCV to work can be a challenge, so I highly recommend you clone:  https://github.com/jayrambhia/Install-OpenCV and let it do all the heavy lifting for you.

If you are using windows or mac, openCV should be a snap to get.  Just head over to:  http://opencv.org/

#how to run:

making this tool work should be a snap.  Simply move some files into the preprocessed directory and then run python process_images.py from the top level directory.  You should see any pictures with faces in the withFace directory.  

Note:  All pictures in preprocessed will be converted to .png's if you want to avoid making this permanent PLEASE copy instead of moving pictures into this directory.
