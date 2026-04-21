def youtubedlp(youtube_url, download_path):
    import yt_dlp
    import os
    #youtube_url = youtube_url.split("=")[1]
    URLS = [youtube_url]
    ydl_opts = {
        'headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    },
        'format': 'm4a/bestaudio/best',
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }],
        'outtmpl': download_path + '%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
    'retries': 10,  # Increase retry count
    'fragment_retries': 10,  # Retry individual fragments if they fail
    'sleep_interval': 1,  # Add sleep interval between retries
    'max_sleep_interval': 5  # Max sleep interval between retries
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(URLS)
        info = ydl.extract_info(URLS[0], download=True)
        print("info", info)
        filename = info.get('requested_downloads')[0].get('filepath')
        print("filename", filename)
    file_path = os.path.join(download_path, f"{filename}")
    return info, file_path