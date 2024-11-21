# YouTube Video Downloader

A YouTube video downloader built with Python's Flask web framework and PyTube. This application allows users to download videos from YouTube by providing a video URL.

## Features

- Enter a YouTube video URL to download the video.
- Download the highest resolution available for the video.
- Provides a simple and easy-to-use web interface.

## Technologies Used

- **Python**: A high-level programming language.
- **Flask**: A lightweight WSGI web application framework for Python.
- **PyTube**: A Python library for downloading YouTube videos.

## Installation

### Prerequisites

- Python 3.6+
- `pip` (Python package manager) to install dependencies.

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/tamipu/video-download.git
   cd youtube-download
   ```

2. **Run the Application**:
   To start the Flask server, run the following command:
   ```bash
   python cd-download.py
   ```
   The app will run on `http://127.0.0.1:5000/`.

## Usage

1. Open your browser and navigate to `http://127.0.0.1:5000/`.
2. Enter a YouTube video URL in the input field.
3. Click **Download** to start the download process.
4. The video will be downloaded to the `output` folder on the local machine.
   
## License

MIT License.
