from ayv import YouTube
from ayv.errors import QuotasExceededException


youtube = YouTube()
client_secrets_file = '/home/lyle/Downloads/python_learning_site.json'
youtube.authenticate_from_client_secrets_file(client_secrets_file)
videos = youtube.search_videos('python programming')
# try:
#     playlists = youtube.search_playlists('python programming')
# except QuotasExceededException:
#     playlists = []
# channels = youtube.search_channels('python programming')
# playlists = youtube.search_playlists('python programming')

if __name__ == '__main__':
    for video in videos:
        print(video.to_dict())
        print()