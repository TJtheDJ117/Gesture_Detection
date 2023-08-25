import mediapipe as mp
import cv2
import os
import matplotlib.pyplot as plt
import pickle
import numpy as np

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)


data = []
dict = {}
labels = []
for letter in os.listdir("C:/Users/tomja/Downloads/Trial"):
    for image in os.listdir("C:/Users/tomja/Downloads/Trial/" + letter):
        data_aux = []
        img = cv2.imread("C:/Users/tomja/Downloads/Trial/" +  letter + "/" + image)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x)
                    data_aux.append(y)
        data.append(data_aux)
        print(image)

dict[letter] = data
try :
    array2 = np.asarray(dict[letter])
except:
    print("ERROR")
else:
    print("WORKED")
