#from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2,time

video = cv2.VideoCapture(0)
while(True):
    check,im = video.read()
    decodedObjects = pyzbar.decode(im)
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data, '\n')
    if(len(decodedObjects) != 0):
        break
    for decodedObject in decodedObjects:
        points = decodedObject.polygon
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points

        n = len(hull)
        for j in range(0, n):
            cv2.line(im, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

            # Display results
    cv2.imshow("Results", im);
    key = cv2.waitKey(1)
    if (key == ord('q')):
        video.release()
        break
cv2.destroyAllWindows()
