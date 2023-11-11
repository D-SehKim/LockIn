import capture
import cv2
import time
import keras

cap = capture.Capture()
cap.open_capture()
last = time.time()

# model = keras.models.load_model('eye_model.keras')

while True:
    if time.time() > last + 0.5:    # update every 0.5 s
        last = time.time()
        cap.display(True)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break