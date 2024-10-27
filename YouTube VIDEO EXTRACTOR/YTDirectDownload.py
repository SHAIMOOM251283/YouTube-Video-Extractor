import yt_dlp

class DownloadVideo:

    def __init__(self):
        self.video_url = input("Enter URL: ")

    def download_video(self):
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.video_url])
            
if __name__ == '__main__':
    YouTube = DownloadVideo()
    YouTube.download_video()