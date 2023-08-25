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

#os.remove("C:/Users/tomja/Downloads/Trial/A1.jpg")
dir_path = "C:/Users/tomja/Downloads/Trial/A"
count = 0
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
print('File count:', count)
"""
data = []
data_sub = []
dict = {}
labels = []
for letter in os.listdir("C:/Users/tomja/Downloads/Trial"):
    for image in os.listdir("C:/Users/tomja/Downloads/Trial/" + letter):
        data_aux = []
        img = cv2.imread("C:/Users/tomja/Downloads/Trial/" + letter + "/" + image)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x)
                    data_aux.append(y)
        data_sub.append(data_aux)
        dict[letter] = data_sub
        try :
            array2 = np.asarray(dict[letter])
        except:
            print("ERROR")
            path = os.path.join("C:/Users/tomja/Downloads/Trial/" + letter + "/", image)
            os.remove(path)
            print(image + " DELETED")
            data_sub = data.copy()
        else:
            data = data_sub.copy()
"""

print("DONE")
