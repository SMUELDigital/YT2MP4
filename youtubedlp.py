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