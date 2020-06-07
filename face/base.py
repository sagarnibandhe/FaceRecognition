import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xff == ord("q"):
        break

# When everything done release capture
cap.release()
cv2.destroyAllWindows()
