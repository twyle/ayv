from setuptools import find_packages, setup

VERSION = '0.0.1' 
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

setup(
    name='youtube',
    packages=find_packages(
        include=[
            'youtube', 
            'youtube.youtube_resources',
            'youtube.youtube_resources.youtube_channel',
            'youtube.youtube_resources.youtube_comment',
            'youtube.youtube_resources.youtube_comment_thread',
            'youtube.youtube_resources.youtube_playlist',
            'youtube.youtube_resources.youtube_video',
            'youtube.youtube_resources.youtube_video_category',
            'youtube.oauth',
            'youtube.search',
            'youtube.search.category',
            'youtube.search.channel',
            'youtube.search.playlist',
            'youtube.search.video'
        ]
        ),
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='Lyle Okoth',
    author_email='lyceokoth@gmail.com',
    license='MIT',
    install_requires=['google-api-python-client==2.81.0', 'google-auth-oauthlib==1.0.0'],
    
    keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)