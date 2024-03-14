from pytube import YouTube

# Download audio from YouTube
def download_audio(youtube_url):
    yt = YouTube(youtube_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(filename='temp_audio')
    return 'temp_audio.mp4'  # pytube saves as mp4 by default