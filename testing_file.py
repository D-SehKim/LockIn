import capture
import cv2
import time
import keras
import create_data_from_image

cap = capture.Capture()
cap.open_capture()
last = time.time()

model = keras.models.load_model('eye_model.h5')
model.load_weights('eye_model.h5', False)

data = create_data_from_image.make_csv(0) # 0 is closed

print(model.predict(data))

while True:
    cap.display(True)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break