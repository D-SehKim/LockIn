import capture
import face_tracking

import cv2
import time
import keras
import create_data_from_image

cap = capture.Capture()
cap.open_capture()

while True:
    frame = cap.get_frame()
    frame = face_tracking.draw_boxes(frame, face_tracking.find_faces(frame))
    cap.display(frame, True)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break