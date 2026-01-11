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
   
  

Example Usage: 
  ```bash
python3 youtube2mp3.py playlist "https://youtube.com/playlist?list=PLDeX5vvsDEZ4G02MZ7iYNW2-5kDlUMyqm&si=0l7GrXRi52P5PCK4" "C:\\Users\\garfi\\Music\\"
```
