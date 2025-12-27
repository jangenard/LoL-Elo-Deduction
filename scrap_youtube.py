from googleapiclient.discovery import build

api_key = 'AIzaSyDFMNW2XTro4Iyr1f0GAA91Ezh1z5N7UvA'
youtube = build('youtube', 'v3', developerKey=api_key)

def search_videos(query):
    videos = []
    for streamer in query : 
        request = youtube.search().list(
            type='video',
            q=streamer,
            part='snippet',
            maxResults=10,
        )
        response = request.execute()
        for item in response['items']:
            if item['id']['kind'] != 'youtube#video':
                continue

            video_id = item['id']['videoId']
            videos.append(video_id)
            print(f"Title: {item['snippet']['title']}")
            print(f"Video ID: {video_id}")
            print(f"Thumbnail URL: {item['snippet']['thumbnails']['high']['url']}")
            print("-" * 50)
    return videos


import yt_dlp

def download_videos(video_urls):
    for vid in video_urls :
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'video.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([vid])
            

def main() :
    streamer_list = ["RATIRL"]
    videos = search_videos(streamer_list)
    urls = ["https://www.youtube.com/watch?v="+i for i in videos]
    print(urls[:1])

    download_videos(urls)


if __name__ == "__main__" :
    main()