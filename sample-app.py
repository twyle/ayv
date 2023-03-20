from ayv import YouTube


youtube = YouTube(credentials_file='/home/lyle/Downloads/client_secret.json', 
                  token_path='')
youtube_client = youtube.get_youtube()
videos = youtube.search_videos('python programming')


if __name__ == '__main__':
    for video in videos:
        print(video.get_video_id())
        print(video.get_video_title())
        print(video.get_video_banner())
        print()