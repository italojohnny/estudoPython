import numpy as np
import cv2

cap = cv2.VideoCapture("video.avi")

ret, frame = cap.read()
while ret:
    # Capture frame-by-frame

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)

    if cv2.waitKey(10) == 27: break

    ret, frame = cap.read()
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

