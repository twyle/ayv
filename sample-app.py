from ayv import YouTube


youtube = YouTube()
client_secrets_file = '/home/lyle/Downloads/client_secret.json'
youtube_client = youtube.authenticate_from_client_secrets_file(client_secrets_file)
videos = youtube.search_videos('python programming')
playlists = youtube.search_playlists('python programming')
channels = youtube.search_channels('python programming')
print(channels)

if __name__ == '__main__':
    for video in videos:
        print(video.get_video_id())
        print(video.get_video_title())
        print(video.get_video_banner())
        print()