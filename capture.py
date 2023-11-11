import cv2

def open_capture(self):
    capture = cv2.VideoCapture(0)                                   # Open webcam

    if not capture.isOpened():                                      # Check if webcam was opened correctly
        print("Error: Could not open webcam.")
        return None
        return capture
    
def close_capture(self, capture):
    capture.release()                                               # Release the webcam, close  window
    cv2.destroyAllWindows()

def get_frame(self, capture):
    was_read, frame = capture.read()

    if not was_read:                                                # Check if frame was read successfully
        print("Error: Could not read frame.")
        return None

    return frame