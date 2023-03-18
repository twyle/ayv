from .oauth import Authenticate


class YouTube:
    def __init__(self, credentials_file='', token_path=''):
        self.__auth = Authenticate(credentials_file, token_path)
        self.__youtube_client = self.__youtube_client = self.__auth.authenticate()

    def get_youtube(self):
        return self.__youtube_client