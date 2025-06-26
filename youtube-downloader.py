from pytubefix import YouTube
from pytubefix.cli import on_progress

# Replace 'url' with your video URL
url = "Enter Video Url"

try:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(f"Video Title: {yt.title}")
    
    # Get the highest resolution stream
    ys = yt.streams.get_highest_resolution()
    
    # Download the video
    ys.download()
    print("Download completed successfully!")
    
except Exception as e:
    print(f"An error occurred: {e}")
