import yt_dlp
import os

def download_video_extract_audio(url, output_filename):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_filename,
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=mR8TS7kkFEk"
    output_filename = "audio_file.m4a"
    download_video_extract_audio(youtube_url, output_filename)
