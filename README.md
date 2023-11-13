# LockIn - Image Processing

### Overview
LockIn uses the computer's webcam to detect when the user's attention leaves the screen in front of them.  
The program:
- Uses the OpenCV library to obtain webcam data in the form of images,
- Feeds the images into a Keras neural network to detect a face,
- Processes the image to isolate the eyes of the user, and
- Feeds images of the user's eyes into a second neural network to predict if the user is looking at the screen

### Installation and Use
Fork the project and run testing_file.py.  
Requires the NumPy, Pandas, Keras, OpenCV, Python Imaging Library, Serial, Plyer, and Pygame libraries.

### Contributors
Ashley Chan  
Andre Gilbertson  
Daniel Kim  
Ian Mei  
Ethan Pham  

Created during the HackUMass 2023 hackathon.
