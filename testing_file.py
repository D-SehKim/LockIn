import capture
import cv2
import time
import keras
import create_data_from_image
import model_test

cap = capture.Capture()
cap.open_capture()
last = time.time()

model = keras.models.load_model('eye_model_better.h5')
model.load_weights('eye_model_better.h5', False)

model_test.model_testing('images/eye_open.jpg', model)

while True:
    cap.display(True)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break