import capture
import face_tracking

import cv2
import time
import notif
import keras
import create_data_from_image
import model_test
import serial

cap = capture.Capture()
cap.open_capture()
last = time.time()

model = keras.models.load_model('eye_model_better8.h5')
model.load_weights('eye_model_better8.h5', False)
predictions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
arduino = serial.Serial('/dev/cu.usbmodem14201',115200,timeout=1)
def summation(sum_list):
    list_sum = 0

    for num in sum_list:
        list_sum += num
    
    return list_sum

def list_and_add():

    predictions.pop(0)
    predictions.append(model_test.model_testing(frame, model))
    #print(predictions)
    list_sum = summation(predictions)

    if list_sum >= 10:
        #return True
        arduino.write(b't')
        predictions.pop(0)
        predictions.append(0)
        notif.play_mp3('alarm_sound_effect.mp3')



while True:
    frame = cap.get_frame()
    frame = face_tracking.draw_boxes(frame, face_tracking.find_faces(frame))
    cap.display(cap.get_frame(), (summation(predictions)<9))
    list_and_add()


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break