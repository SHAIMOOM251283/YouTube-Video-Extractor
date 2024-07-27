import yt_dlp

class DownloadVideo:

    def __init__(self):
        self.url = input("Enter URL: ")
        self.output_path = input("Enter Output Path: ")

    def download_video(self):
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Download best quality video and audio
            'outtmpl': '%(title)s.%(ext)s',  # Save file with video title and extension
            'progress_hooks': [lambda d: print('Download completed successfully!') if d['status'] == 'finished' else print(f"Downloading... {d['_percent_str']} of {d['_total_bytes_str']}", end='\r')],  # Show download progress inline
        }

        if self.output_path:
            ydl_opts['outtmpl'] = self.output_path + '/%(title)s.%(ext)s'

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([self.url])
            except yt_dlp.utils.DownloadError as e:
                print(f"An error occurred: {e}")

if __name__ == '__main__':
    YouTube = DownloadVideo()
    YouTube.download_video()