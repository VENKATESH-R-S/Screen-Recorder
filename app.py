import cv2
import pyautogui
from flask import Flask, render_template, send_file
from threading import Thread
import time
import numpy as np 

app = Flask(__name__)

# Define the video writer
video_writer = None

# Flag to indicate whether to record or not
recording = False

# Function to start recording
def start_recording():
    global recording, video_writer

    # Set up the video writer
    video_writer = cv2.VideoWriter("recording.avi", cv2.VideoWriter_fourcc(*"XVID"), 20, pyautogui.size())

    # Start recording
    while recording:
        screenshot = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        video_writer.write(frame)

        time.sleep(0.05)  # Adjust the delay based on your needs

    # Release the video writer
    video_writer.release()

# Route to start recording
@app.route("/start")
def start():
    global recording
    recording = True

    # Start recording in a separate thread
    Thread(target=start_recording).start()

    return "Recording started"

# Route to stop recording
@app.route("/stop")
def stop():
    global recording
    recording = False
    return "Recording stopped"


@app.route("/serve_video")
def serve_video():
    return send_file("recording.avi", as_attachment=True)

# Route to view the recorded video
@app.route("/")
def view():
    return render_template("index.html")

# Route to download the recorded video
@app.route("/download")
def download():
    return send_file("recording.avi", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True,port=8000)
