from compare import dhash, hamming_distance
from face_detect import face_detection
from PIL import Image
import sys

picture = sys.argv[1]
casc_path = sys.argv[2]

facesNumber = face_detection(picture, casc_path)

if facesNumber == 1:
    print dhash(Image.open('cropped_0.png'))
else:
    print 'More than one faces or noone have been discovered.'
    print dhash(Image.open(picture))
