import cv2
from fer import FER
import streamlit as st
import numpy as np
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser  # To open the Spotify link in the browser
import time
from dotenv import load_dotenv
import os


load_dotenv()

# Spotify authentication using Client ID and Client Secret
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Streamlit UI header
st.title("Emotion Detection and Music Recommendation")

# Initialize the video capture
video = cv2.VideoCapture(0)

if not video.isOpened():
    st.error("Error: Could not access the webcam.")
else:
    # Load the pre-trained Haar Cascade Classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Display the webcam feed and capture button
    stframe = st.empty()  # Empty frame for webcam feed

    captured_image = None
    emotion_placeholder = st.empty()
    detected_emotion = ""

    # Streamlit button to capture the image
    if st.button('Capture Image'):
        check, frame = video.read()
        if check:
            # Save the captured frame
            cv2.imwrite("filename.jpg", frame)
            captured_image = frame

    # Show the captured image and perform emotion detection
    if captured_image is not None:
        # Convert the frame to grayscale
        gray = cv2.cvtColor(captured_image, cv2.COLOR_BGR2GRAY)

        # Calculate the average brightness of the frame
        avg_brightness = np.mean(gray)

        # Set a brightness threshold to detect black screen (you can adjust the value if needed)
        brightness_threshold = 20  # A value close to 0 indicates a very dark image

        if avg_brightness < brightness_threshold:  # If the average brightness is very low
            st.error("Error: Camera feed is black or obstructed. Please check if the camera shutter is open or the camera is blocked.")
        else:
            # Detect faces in the image
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Create an emotion detector
            detector = FER()

            if len(faces) == 0:
                st.warning("No faces detected. Please ensure the camera is properly positioned.")
            else:
                # For each face detected, perform emotion detection
                for (x, y, w, h) in faces:
                    # Get the region of interest (ROI) for emotion detection
                    roi = captured_image[y:y + h, x:x + w]

                    # Ensure the ROI is valid before performing emotion detection
                    if roi is not None and roi.size > 0:
                        # Detect emotions on the face
                        emotions = detector.top_emotion(roi)

                        # Draw a rectangle around the face
                        cv2.rectangle(captured_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

                        # Check if emotions are detected and score is not None
                        if emotions and emotions[1] is not None:
                            emotion, score = emotions
                            cv2.putText(captured_image, f"{emotion} ({score:.2f})", (x, y - 10),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

                            detected_emotion = f"Detected Emotion: {emotion} ({score:.2f})"
                            emotion_placeholder.subheader(detected_emotion)

                            # Redirect to Spotify based on detected emotion
                            if emotion == 'happy':
                                st.write("Redirecting to a Happy Playlist on Spotify...")
                                webbrowser.open('https://open.spotify.com/playlist/37i9dQZF1DXbpR3uCBnjpF?si=c88f935e161040e2')
                            elif emotion == 'sad':
                                st.write("Redirecting to a Sad Playlist on Spotify...")
                                webbrowser.open('https://open.spotify.com/playlist/37i9dQZF1DWSqBruwoIXkA?si=1b74fb9e88644f0e')
                            elif emotion == 'angry':
                                st.write("Redirecting to an Angry Playlist on Spotify...")
                                webbrowser.open('https://open.spotify.com/playlist/37i9dQZF1EIhuCNl2WSFYd?si=1625fb349763454d')
                            elif emotion == 'neutral':
                                st.write("Redirecting to a Neutral Playlist on Spotify...")
                                webbrowser.open('https://open.spotify.com/playlist/1AeFZFriVLanHvczecFJ2J?si=7e5e36808677413d')
                            elif emotion == 'surprise':
                                st.write("Redirecting to a Neutral Playlist on Spotify...")
                                webbrowser.open('https://open.spotify.com/playlist/1AeFZFriVLanHvczecFJ2J?si=7e5e36808677413d')
                            elif emotion == 'surprise':
                                st.write("Redirecting to a Neutral Playlist on Spotify...")
                                webbrowser.open('https://open.spotify.com/playlist/1DrCrdRmpDHUstrc2jOIF6?si=aea0f8ea0a1c48f5')

                        else:
                            # Handle case when no valid emotion is detected
                            cv2.putText(captured_image, "Emotion not detected", (x, y - 10),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
                    else:
                        st.error("Error: Invalid region of interest for emotion detection.")

    # Convert to RGB for Streamlit
    if captured_image is not None:
        image_bgr = cv2.cvtColor(captured_image, cv2.COLOR_BGR2RGB)
        st.image(image_bgr, caption="Detected Emotion", use_container_width=True)

        if detected_emotion:
            st.subheader(detected_emotion)

    else:
        # Display webcam feed if no image has been captured
        check, frame = video.read()
        if check:
            stframe.image(frame, channels="BGR", use_container_width=True)

# Release the video capture after the process
video.release()
