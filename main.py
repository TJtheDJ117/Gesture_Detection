import cv2
import mediapipe as mp

#drawing lines between the landmarks
mp_draw = mp.solutions.drawing_utils
mp_draw_styles = mp.solutions.drawing_styles


mp_hands = mp.solutions.hands

#Open camera feed
capture = cv2.VideoCapture(0)

hands = mp_hands.Hands()

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

    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)

    results = hands.process(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow('Frame', frame)
    #If 'q' key is pressed, break out of the loop
    if cv2.waitKey(1) == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()

