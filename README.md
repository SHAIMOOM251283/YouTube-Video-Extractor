# YouTube Video Extractor

## Overview
YouTube Scraper is a powerful tool designed to download YouTube videos effortlessly using the yt-dlp library. This project includes three distinct scripts, allowing users to download videos with default settings, specify a custom output path for greater flexibility, and convert downloaded videos from `.webm` to `.mp4` format.

## Features
- **High-Quality Downloads**: Download videos in the best quality available, combining the best video and audio streams.
- **Automatic File Naming**: Save videos with their original title and extension for easy identification.
- **Custom Output Path**: Option to specify an output directory for downloaded videos, providing organizational flexibility.
- **Robust Error Handling**: Effective error management to ensure smooth and reliable downloading.
- **Video Conversion**: Convert downloaded `.webm` files to `.mp4` format using the `convert_to_mp4.py` script.

## Scripts

1. **YTDirectDownload.py:**
   - Downloads YouTube videos in the best available quality (video + audio).
   - Saves the file with its original title and extension.
   - Requires only the video URL for the download.

2. **YTVideoExtractor.py:**
    - Downloads YouTube videos in the best quality with user-defined output path.
    - Saves the file with its original title and extension.
    - Includes error handling for download failures.

3. **convert_to_mp4.py**: 
    - Converts downloaded `.webm` videos to `.mp4` format using the `ffmpeg` tool.
    - The script prompts the user for the video file name (without extension) and automatically converts the `.webm` file to `.mp4`.
    - Handles errors during the conversion process to ensure a smooth experience.

## Example Usage

### YouTube Video Downloader:
- Run the script to download YouTube videos with default settings or specify a custom output path.

### Video Conversion (convert_to_mp4.py):
- Execute the script and input the file name (without extension) to convert a `.webm` video to `.mp4`.

## Contributing
Feel free to fork this repository, make changes, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.