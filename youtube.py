import streamlit as st
from pytube import YouTube, Playlist

# Title and input box for URL and video Quality
st.title("Youtube Video Downloader")

url=st.text_input("Enter the YouTube URL")
is_playlist=st.checkbox("Is this a Playlist?")
resolution=st.selectbox("Select the resolution",["2160p","1080p","720p","480p","360p","240p","144p"])

# Define a function to download a single video
def download_video(url, resolution):
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension="mp4", res=resolution).first()
    if video:
        video.download()
        st.success(f"Downloaded: {yt.title}")
    else:
        st.error("Video not available in the selected resolution.")

#Define a function to download a playlist
def download_playlist(url, resolution):
    playlist = Playlist(url)
    for video_url in playlist.video_urls:
        download_video(video_url, resolution)

#Add a download button and call the appropriate function based on the user's input
if st.button("Download"):
    if is_playlist:
        download_playlist(url, resolution)
    else:
        download_video(url, resolution)

