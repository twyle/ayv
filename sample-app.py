from youtube import YouTube


youtube = YouTube(credentials_file='/home/lyle/Downloads/client_secret.json', 
                  token_path='')
# videos = youtube.search_videos('python programming')
# related_videos = youtube.find_related_videos(videos[0]) 
# most_popular_ke_videos = youtube.find_most_popular_videos_by_region('ke')
# video_categories = youtube.get_video_categories()
film_animation = youtube.find_most_popular_videos_by_category('1')

if __name__ == '__main__':
    print('works')
    print(film_animation)