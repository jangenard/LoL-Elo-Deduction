import requests

CLIENT_ID = 'YOUR_CLIENT_ID'
OAUTH_TOKEN = 'YOUR_OAUTH_TOKEN'

headers = {
    'Client-ID': CLIENT_ID,
    'Authorization': f'Bearer {OAUTH_TOKEN}'
}

def search_clips(query):
    url = f'https://api.twitch.tv/helix/clips?game={query}&first=5'
    response = requests.get(url, headers=headers)
    data = response.json()

    for clip in data['data']:
        print(f"Clip Title: {clip['title']}")
        print(f"Clip URL: {clip['url']}")
        print(f"Thumbnail URL: {clip['thumbnail_url']}")
        print("-" * 50)

search_clips('game_name')  # Replace with your search query
