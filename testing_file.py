import capture
import face_tracking

import cv2
import time
import keras
import create_data_from_image
import model_test

cap = capture.Capture()
cap.open_capture()
last = time.time()

model = keras.models.load_model('eye_model_better5.h5')
model.load_weights('eye_model_better5.h5', False)



while True:
    frame = cap.get_frame()
    frame = face_tracking.draw_boxes(frame, face_tracking.find_faces(frame))
    cap.display(frame, True)
    
    model_test.model_testing(cap.get_frame(), model) # 0 is closed

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break