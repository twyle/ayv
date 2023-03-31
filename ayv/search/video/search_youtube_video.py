from ..youtube_search import YouTubeSearch
from ..search_type import YouTubeSearchType
# from .video_search_query import YouTubeVideoSearchQuery
from ..search_query import YouTubeSearchQuery
from .find_video import FindVideo
from ...youtube_resources.youtube_video import YouTubeVideoCollection

class VideoSearch(YouTubeSearch):
    __MAX_RESULTS = 10
    __REGION_CODE = 'US'
    
    def __init__(self, youtube_client):
        self.__youtube_client = youtube_client
        self.__type = YouTubeSearchType.VIDEO
        self.__query = ''
        self.__videos = YouTubeVideoCollection()
        
    def __get_query(self):
        return self.__query.query_string
    
    def get_videos(self):
        return self.__videos
        
    def basic_info(self):
        basic_info_params = self.__generate_basic_info_params()
        return basic_info_params
    
    def advanced_info(self):
        pass
    
    def all_info(self):
        pass
    
    def __generate_basic_info_params(self):
        basic_info_params = dict(
            part='id',
            type=self.__type,
            q=self.__get_query(),
            maxResults=self.__MAX_RESULTS,
            regionCode=self.__REGION_CODE
        ) 
        return basic_info_params
    
    def __generate_basic_info_params_for_related_video(self, video_id):
        basic_info_params = dict(
            part='id,snippet',
            type=self.__type,
            relatedToVideoId=video_id,
            maxResults=self.__MAX_RESULTS,
            regionCode=self.__REGION_CODE
        ) 
        return basic_info_params
    
    def __generate_basic_info_params_for_most_popular_video_by_region(self, 
                region_code):
        basic_info_params = dict(
            part='id,snippet',
            chart='mostPopular',
            regionCode=region_code
        ) 
        return basic_info_params
    
    def __generate_basic_info_params_for_most_popular_video_by_category(self, 
                category_id):
        basic_info_params = dict(
            part='id,snippet',
            chart='mostPopular',
            videoCategoryId=category_id
        ) 
        return basic_info_params
    
    def search_videos(self, query_string: str, next_page_token=None):
        self.__query = YouTubeSearchQuery(query_string)
        basic_info_params = self.__generate_basic_info_params()
        if next_page_token:
            basic_info_params['pageToken'] = next_page_token
        search_request = self.__youtube_client.search().list(
            **basic_info_params
        )
        search_response = search_request.execute()
        (previous_page_token, next_page_token, videos) = self.__parse_basic_response(search_response)
        return (previous_page_token, next_page_token, videos)
    
    def __parse_basic_response(self, search_response):
        videos = []
        previous_page_token = search_response.get('prevPageToken', '')
        next_page_token = search_response.get('nextPageToken', '')
        video_results = search_response['items']
        for video_result in video_results:
            video_id = video_result['id']['videoId']
            youtube_video = FindVideo(self.__youtube_client).find_video(video_id)
            videos.append(youtube_video)
        self.__videos.add_videos(videos)
        return (previous_page_token, next_page_token, videos)
    
    def __parse_basic_response_popular_videos(self, search_response):
        videos = []
        video_results = search_response['items']
        for video_result in video_results:
            if video_result.get('id'):
                video_id = video_result['id']
            else:
                video_id = video_result['id']['videoId']
            youtube_video = FindVideo(video_id).find_video(self.__youtube_client)
            videos.append(youtube_video)
        return videos
    
    def search_related_videos(self, youtube_video, youtube_client, search_type='basic'):
        search_response = None
        if search_type == 'basic':
            basic_info_params = self.__generate_basic_info_params_for_related_video(youtube_video.get_video_id())
            search_request = youtube_client.search().list(
                **basic_info_params
            )
            search_response = search_request.execute()
            videos = self.__parse_basic_response(search_response, youtube_client)
        return videos
    
    def search_most_popular_videos_by_region(self, region_code, youtube_client, search_type='basic'):
        search_response = None
        if search_type == 'basic':
            basic_info_params = self.__generate_basic_info_params_for_most_popular_video_by_region(region_code)
            search_request = youtube_client.videos().list(
                **basic_info_params
            )
            search_response = search_request.execute()
            videos = self.__parse_basic_response_popular_videos(search_response, youtube_client)
        return videos
    
    def search_most_popular_videos_by_category(self, category_id, youtube_client, search_type='basic'):
        search_response = None
        if search_type == 'basic':
            basic_info_params = self.__generate_basic_info_params_for_most_popular_video_by_category(category_id)
            search_request = youtube_client.videos().list(
                **basic_info_params
            )
            try:
                search_response = search_request.execute()
                videos = self.__parse_basic_response_popular_videos(search_response, youtube_client)
            except:
                videos = []
        return videos