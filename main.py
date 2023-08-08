import cv2
import numpy as np

#Open camera feed
capture = cv2.VideoCapture(0)

#Create a background detector(#of previous frames to make background model, #how much pixel change to say it is a valid change, detect shadows)
fgbg = cv2.createBackgroundSubtractorMOG2(300, 400, True)
frameCount = 0

#print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

#If camera feed is mot opened
if not capture.isOpened():
    print("Cannot open camera")
while(1):

    #Return the frame
    ret, frame = capture.read()

    #If frame is not returned print error message and break
    if not ret:
        print("Can't recieve frame")
        break
    #count frames
    frameCount += 1

    #Get foreground mask
    fgmask = fgbg.apply(frame)

    #Count all non zero pixals within the mask
    count = np.count_nonzero(fgmask)

    print('Frame : %d, Pixel Count: %d' % (frameCount, count))

    #If it is not the first frame and if the changed pixels count is greater than 1000 count it as a hand in the frame
    if(frameCount > 1 and count > 1000):
        cv2.putText(frame, 'I SEE THE HAND', (500, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', fgmask)

    #If 'q' key is pressed, break out of the loop
    if cv2.waitKey(1) == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()

