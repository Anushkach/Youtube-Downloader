import streamlit as st
from pytube import YouTube, Playlist
import tempfile
import os

# Title and input box for URL and video Quality
st.title("Youtube Video Downloader")

url = st.text_input("Enter the YouTube URL")
is_playlist = st.checkbox("Is this a Playlist?")
resolution = st.selectbox("Select the resolution", ["2160p", "1080p", "720p", "480p", "360p", "240p", "144p"])

# Define a function to download a single video
def download_video(url, resolution):
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension="mp4", res=resolution).first()
    if video:
        temp_dir = tempfile.mkdtemp()
        video.download(temp_dir)
        return os.path.join(temp_dir, video.default_filename)
    else:
        st.error("Video not available in the selected resolution.")
        return None

# Define a function to download a playlist
def download_playlist(url, resolution):
    playlist = Playlist(url)
    downloaded_files = []
    for video_url in playlist.video_urls:
        file_path = download_video(video_url, resolution)
        if file_path:
            downloaded_files.append(file_path)
    return downloaded_files

# Add a download button and call the appropriate function based on the user's input
if st.button("Download"):
    if is_playlist:
        downloaded_files = download_playlist(url, resolution)
        for file_path in downloaded_files:
            st.download_button(f"Download {os.path.basename(file_path)}", file_path)
    else:
        file_path = download_video(url, resolution)
        if file_path:
            st.download_button(f"Download {os.path.basename(file_path)}", file_path)
