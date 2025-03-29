# To run this code, ensure you have the required libraries installed:
# Kivy, OpenCV, and NumPy.

# It is recommended to use a virtual environment for this code.
#To run virtual env: python -m venv env && .\env\Scripts\activate

import cv2
import numpy as np
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.lang import Builder


# Define Main Menu Screen
class MainMenu(Screen):
    pass

# Define Face Detection Screen
class FaceDetection(Screen):
    def on_enter(self):
        self.img = self.ids.video_feed  # Reference to Image widget in KV file

        # Load Haarcascade Models
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

        # Start Video Capture
        self.cap = cv2.VideoCapture(0)  # Change to 1 if using an external webcam

        # Schedule frame update
        Clock.schedule_interval(self.update, 1.0 / 30.0)  # 30 FPS

    def update(self, dt):
        ret, frame = self.cap.read()
        if ret:
            # Convert to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (5, 94, 255), 5)
                cv2.putText(frame, "UCC STUDENT", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]

                # Detect eyes
                eyes = self.eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

            # Convert OpenCV image (BGR) to RGB for Kivy
            frame = cv2.flip(frame, 0)  # Flip the image to correct orientation
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB
            buf = frame.tobytes()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='rgb')
            texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')

            # Update Image widget
            self.img.texture = texture

    def on_leave(self):
        Clock.unschedule(self.update)  # Stop updating
        self.cap.release()  # Release the camera

Builder.load_file("FaceApp.kv")

# Create Screen Manager
class FaceDetectionApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name="main_menu"))
        sm.add_widget(FaceDetection(name="face_detect"))
        return sm

if __name__ == '__main__':
    FaceDetectionApp().run()
