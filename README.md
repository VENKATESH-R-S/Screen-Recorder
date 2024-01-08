# Screen Recording Web App

This is a simple Flask web application for screen recording using OpenCV and PyAutoGUI.

## Features

- Start and stop screen recording.
- View the recorded video.
- Download the recorded video.

## Requirements

- Python 3.x
- OpenCV
- PyAutoGUI
- Flask

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/screen-recording-web-app.git
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and navigate to [http://localhost:8000](http://localhost:8000).

3. Click the "Start Recording" button to begin recording.

4. To stop recording, click the "Stop Recording" button.

5. View the recorded video by clicking the "View Recorded Video" button.

6. Download the recorded video by clicking the "Download" button.

## Notes

- Adjust the recording delay in the `start_recording` function to control the frame rate.

## Contributors

- Your Name <your.email@example.com>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
