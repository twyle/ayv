from youtube import YouTube


youtube = YouTube(credentials_file='/home/lyle/Downloads/client_secret.json', 
                  token_path='')
youtube_client = youtube.get_youtube()

if __name__ == '__main__':
    print('works')