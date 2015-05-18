import cv2
# import sys


def face_detection(image, casc_path):
    counter = 0

    # Get user supplied values
    # imagePath = sys.argv[1]
    # cascPath = sys.argv[2]

    imagePath = image
    cascPath = casc_path

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30),
       # flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # print "Found {0} faces!".format(len(faces))

    for (x, y, w, h) in faces:
        crop_img = image[y: y + h, x: x + w]
        # print counter
        cv2.imwrite('cropped_{0}.png'.format(counter), crop_img)
        # cv2.imshow("cropped_{0}".format(counter), crop_img)
        counter = counter + 1
        # cv2.waitKey(0)
        
    '''
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Faces found", image)
    cv2.waitKey(0)
    '''

    return len(faces)
