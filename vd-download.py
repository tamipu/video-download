import os
from pytube import YouTube
from sys import argv

output_path = "./../output videos"
os.makedirs(output_path, exist_ok=True)

try:
    yt = YouTube(argv[1])

    stream = yt.streams.get_highest_resolution()

    stream.download(output_path)

    print(f"Video downloaded successfully to {output_path}")

except IndexError:
    print("Please provide a YouTube video URL as an argument.")
except Exception as e:
    print(f"An error occurred: {e}")
