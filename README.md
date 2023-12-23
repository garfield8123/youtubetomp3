## **Youtube to M4A Automatica Downloader with Artist Name and Song Title (If Applicable)**
- Channel : Download all youtube videos in the channel and convert them to m4a audio files
    - Channel <Channel_id> <Download_Location> : Full parameters to convert youtube channel to m4a
        - Channel_id : the channel Id of the youtube user in which you would like to download all the videos from
        - Download_location : The full path of where you would the downloaded m4a files to be stored 
- Playlist : Downloads all youtube videos in the whole playlist
  - Playlist <Playlist_url > <Download_Location> : Full parameters to convert youtube playlist to m4a
      - Playlist_url : the playlist url of the youtube playlist in which you would like to download all the videos from
      - Download_location : The full path of where you would the downloaded m4a files to be stored 
- Video : Downloads the single youtube video into a m4a. 
  - Video <Video_url> <Download_Location> : Full parameters to convert youtube video to m4a
      - Video_url : the video url of the youtube video in which you would like to download all the videos from
      - Download_location : The full path of where you would the downloaded m4a files to be stored
   

- NOTE:
  - To get Artist Name and Song Title Correctly video title must be in this format:
    - <Artist_name> - <song-title>
  ```python
  # Splits the song title by "-" 
  title_parts = video.split('-')

    if len(title_parts) >= 2:
        # Grabs the respectful artist_name and song_title 
        artist_name = title_parts[0].strip()
        track_title = title_parts[1].strip()
        print(f"Artist Name: {artist_name}")
        print(f"Track Title: {track_title}")
  ```
  

Example Usage: 
  ```bash
python3 youtube2mp3.py playlist "https://youtube.com/playlist?list=PLDeX5vvsDEZ4G02MZ7iYNW2-5kDlUMyqm&si=0l7GrXRi52P5PCK4" "C:\\Users\\garfi\\Music\\"
```
