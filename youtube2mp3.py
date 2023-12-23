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
            'outtmpl': download_path + '%(title)s.%(ext)s'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download(URLS)
            info = ydl.extract_info(URLS[0], download=False)
        #video_title, video_ext = get_video_info(URLS)
        print(info.get("title"))
        addartisttomusic(download_path, info.get("title"))
        sleep(10)

def youtubevideo2mp3(youtube_url, Download_location):
    download_path = Download_location
    youtube_url = youtube_url.split("=")[1]
    URLS = [youtube_url]

    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [],
        'outtmpl': download_path + '%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(URLS)
        info = ydl.extract_info(URLS[0], download=False)
    addartisttomusic(download_path, info.get("title"))

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
            'outtmpl': download_path + '%(title)s.%(ext)s'
        }
        #video_title, video_ext = get_video_info(video['videoId'])
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download(URLS)
            info = ydl.extract_info(URLS[0], download=False)
        addartisttomusic(download_path, info.get("title"))
        sleep(10)

def get_video_info(URLS):
    with yt_dlp.YoutubeDL() as ydl:
        info = ydl.extract_info(URLS, download=False)
    return info.get('title'), info.get('ext')

def addartisttomusic(download_path, video):
    from mutagen.mp4 import MP4, MP4Cover
    file_path = download_path + f"{video}.m4a"  # Path to the downloaded file
    audio = MP4(file_path)
    # Splitting the title based on the hyphen to get artist and song title
    title_parts = video.split('-')

    if len(title_parts) >= 2:
        # Grabs the respectful artist_name and song_title 
        artist_name = title_parts[0].strip()
        track_title = title_parts[1].strip()
        print(f"Artist Name: {artist_name}")
        print(f"Track Title: {track_title}")
    else:
        print("Couldn't extract the artist name from the title.")

    audio['\xa9ART'] = artist_name # '\xa9ART' is the tag for artist information
    audio['\xa9nam'] = track_title
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
