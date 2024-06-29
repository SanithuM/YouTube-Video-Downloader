from pytube import YouTube
import time

# Ask the user for the video URL
url = input("Enter the video URL: ")

# Create a YouTube object
yt = YouTube(url)

# Print the video title and available streams
print("Title:", yt.title)
print("Available streams:")
for stream in yt.streams.filter(progressive=True):
    print(stream, '(', round(stream.filesize/1024/1024, 2), 'MB)')

# Ask the user for the stream to download
itag = input("Enter the itag of the stream to download: ")

# Download the video
stream = yt.streams.get_by_itag(itag)

start_time = time.time()
stream.download(output_path='videos')
end_time = time.time()

duration = end_time - start_time
print("Download complete!")
print("Download duration:", round(duration, 2), "seconds")





