import cv2

class Capture():
    def __init__(self):
        self.capture = None

    def open_capture(self):
        self.capture = cv2.VideoCapture(0)
        if not self.capture.isOpened():
            print("Error: Could not open webcam.")
        
    def close_capture(self):
        self.capture.release()
        cv2.destroyAllWindows()

    def get_frame(self):
        was_read, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.flip(frame, 1)

        if not was_read:
            print("Error: Could not read frame.")
            return None
        return frame

    def display(self, frame, focused: bool):
        text = "Focused: "
        if focused:
            text += "True"
        else:
            text += "False"

        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)
        cv2.imshow("Webcam", frame)