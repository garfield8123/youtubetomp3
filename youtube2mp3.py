from time import sleep
import scrapetube
import yt_dlp
import sys

#https://youtube.com/playlist?list=PLDeX5vvsDEZ4G02MZ7iYNW2-5kDlUMyqm&si=0l7GrXRi52P5PCK4

def playlist2mp3(playlist_url, Download_location):
    playlist_id = playlist_url.split("=")[1]

    videos = scrapetube.get_playlist(playlist_id)
    download_path = Download_location
    for video in videos:
        print("https://www.youtube.com/watch?v=" + video['videoId'])
        

        URLS = ["https://www.youtube.com/watch?v=" + video['videoId']]

        ydl_opts = {
            'format': 'm4a/bestaudio/best',
            # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
            'postprocessors': [],
            'outtmpl': download_path + '%(title)s.%(ext)s',
            'restrictfilenames': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download(URLS)
            info = ydl.extract_info(URLS[0], download=False)
            filename = ydl.prepare_filename(info)
        #video_title, video_ext = get_video_info(URLS)
        print(filename)
        addartisttomusic(download_path, filename)
        sleep(10)

def youtubevideo2mp3(youtube_url, Download_location):
    import os
    download_path = Download_location
    youtube_url = youtube_url.split("=")[1]
    URLS = [youtube_url]
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [],
        'outtmpl': download_path + '%(title)s.%(ext)s',
        'restrictfilenames': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(URLS)
        info = ydl.extract_info(URLS[0], download=False)
        filename = ydl.prepare_filename(info)
    file_path = os.path.join(download_path, f"{filename}")
    addartisttomusic(info, file_path)

def youtubeChannel2mp3(Channel_id, Download_location):
    videos = scrapetube.get_channel(Channel_id)
    download_path = Download_location
    for video in videos:
        print("https://www.youtube.com/watch?v=" + video['videoId'])
        

        URLS = ["https://www.youtube.com/watch?v=" + video['videoId']]

        ydl_opts = {
            'format': 'm4a/bestaudio/best',
            # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
            'postprocessors': [],
            'outtmpl': download_path + '%(title)s.%(ext)s',
            'restrictfilenames': True
        }
        #video_title, video_ext = get_video_info(video['videoId'])
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download(URLS)
            info = ydl.extract_info(URLS[0], download=False)
            filename = ydl.prepare_filename(info)
        addartisttomusic(download_path, filename)
        sleep(10)

def get_video_info(URLS):
    with yt_dlp.YoutubeDL() as ydl:
        info = ydl.extract_info(URLS, download=False)
    return info.get('title'), info.get('ext')

def addartisttomusic(info, file_path):
    from mutagen.mp4 import MP4, MP4Cover
    audio = MP4(file_path)
    audio['\xa9ART'] = info.get("channel") # '\xa9ART' is the tag for artist information
    audio['\xa9nam'] = info.get("title")
    audio['\xa9alb'] = info.get("album")
    audio['\xa9wrt'] = info.get("uploader")
    audio['desc'] = info.get("description")
    import requests
    audio['covr'] = [MP4Cover(requests.get(info.get("thumbnail")).content, imageformat=MP4Cover.FORMAT_JPEG)]
    audio.save()

if __name__ == "__main__":
    if sys.argv[1] == "-h":
        print('''
        -Channel : Download all youtube videos in the channel and convert them to m4a audio files
            -Channel <Channel_id> <Download_Location> : Full parameters to convert youtube channel to m4a
                - Channel_id : the channel Id of the youtube user in which you would like to download all the videos from
                - Download_location : The full path of where you would the downloaded m4a files to be stored 
        -Playlist : Downloads all youtube videos in the whole playlist
            -Playlist <Playlist_url > <Download_Location> : Full parameters to convert youtube playlist to m4a
                - Playlist_url : the playlist url of the youtube playlist in which you would like to download all the videos from
                - Download_location : The full path of where you would the downloaded m4a files to be stored 
        -Video : Downloads the single youtube video into a m4a. 
            -Video <Video_url> <Download_Location> : Full parameters to convert youtube video to m4a
                - Video_url : the video url of the youtube video in which you would like to download all the videos from
                - Download_location : The full path of where you would the downloaded m4a files to be stored 

        Example Usage: 
              
        python3 youtube2mp3.py playlist "https://youtube.com/playlist?list=PLDeX5vvsDEZ4G02MZ7iYNW2-5kDlUMyqm&si=0l7GrXRi52P5PCK4" "C:\\Users\\garfi\\Music\\"
            
            ''')
    elif "channel" in sys.argv[1].lower():
        #print(sys.argv[2], sys.argv[3])
        if len(sys.argv) != 4:
            print("Usage {} [Channel_Id] [Download_Location]"  .format(sys.argv[0] + " " + sys.argv[1]))
        youtubeChannel2mp3(sys.argv[2], sys.argv[3])
        print("Youtube Channel Download Completed")
        print("Used this youtube Channel: ", sys.argv[2])
        print("All Videos have been downloaded and stored here: ", sys.argv[3])
        print("---------- FINISHED ------------")
    elif "playlist" in sys.argv[1].lower():
        if len(sys.argv) != 4:
            print("Usage {} [playlist_url] [Download_Location]"  .format(sys.argv[0] + " " + sys.argv[1]))
        playlist2mp3(sys.argv[2], sys.argv[3])
        print("Youtube Playlist Download Completed")
        print("Used this Playlist url: ", sys.argv[2])
        print("All Videos have been downloaded and stored here: ", sys.argv[3])
        print("---------- FINISHED ------------")
    else:
        if len(sys.argv) != 4:
            print("Usage {} [youtube_url] [Download_Location]"  .format(sys.argv[0] + " " + sys.argv[1]))
        youtubevideo2mp3(sys.argv[2], sys.argv[3])
        print("Youtube Video Download Completed")
        print("Used this youtube url: ", sys.argv[2])
        print("Video has been downloaded and stored here: ", sys.argv[3])
        print("---------- FINISHED ------------")
