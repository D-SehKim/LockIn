import cv2

detection_model = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def find_faces(frame):
    return detection_model.detectMultiScale(frame, scaleFactor = 1.3, minNeighbors = 5, minSize = (30, 30))

def draw_boxes(frame, faces):
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 5)
    return frame