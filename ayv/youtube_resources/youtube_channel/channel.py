class Channel:
    def __init__(self, id, title, description, customUrl, publishedAt, thumbnails, statistics):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__customUrl = customUrl
        self.__publishedAt = publishedAt
        self.__thumbnails = thumbnails
        self.__statistics = statistics
        
    def get_channel_thumbnail(self):
        thumbnail = ''
        if self.__thumbnails:
            if self.__thumbnails.get('default'):
                thumbnail = self.__thumbnails.get('default').get('url')
            elif self.__thumbnails.get('medium'):
                thumbnail = self.__thumbnails.get('medium').get('url')
            elif self.__thumbnails.get('high'):
                thumbnail = self.__thumbnails.get('high').get('url')
            elif self.__thumbnails.get('standard'):
                thumbnail = self.__thumbnails.get('standard').get('url')
            elif self.__thumbnails.get('maxres'):
                thumbnail = self.__thumbnails.get('maxres').get('url')
        return thumbnail