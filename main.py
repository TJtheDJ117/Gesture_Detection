import cv2
import mediapipe as mp
import pickle
import numpy as np

#drawing lines between the landmarks
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

print("Loaded")
#Open camera feed
capture = cv2.VideoCapture(0)

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

frameCount = 0

#print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
label_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#If camera feed is mot opened 
if not capture.isOpened():
    print("Cannot open camera")
while(1):
    data = []
    x_ = []
    y_ = []

    ret, frame = capture.read()

    #If frame is not returned print error message and break
    if not ret:
        print("Can't recieve frame")
        break

    H, W, _ = frame.shape

    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    data_aux = []
    results = hands.process(frame)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,  # image to draw
                hand_landmarks,  # model output
                mp_hands.HAND_CONNECTIONS,  # hand connections
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())
        
        for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y

                data_aux.append(x)
                data_aux.append(y)
            """
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))
            """
        #list = list(np.asarray(data_aux))
        pred = model.predict([np.asarray(data_aux)])
        pred_char = pred[0]
        cv2.putText(frame, pred_char, (500, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
    #pred_char = int(pred[0])
    cv2.imshow('Frame', cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    #If 'q' key is pressed, break out of the loop
    if cv2.waitKey(1) == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()