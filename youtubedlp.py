"""
Disclaimer:
This script is provided for educational and personal use only.

1. Downloading videos from YouTube may violate its Terms of Service unless you have explicit permission or are using YouTube Premium.
2. The user is responsible for ensuring compliance with local laws and regulations.
3. The author assumes no liability for misuse of this script or any consequences resulting from its use.

Use this script at your own risk.
"""


import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
        'outtmpl': '%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except yt_dlp.utils.DownloadError as e:
            print(f"Error downloading video: {e}")

url = input("Enter your url > ")
download_video(url)