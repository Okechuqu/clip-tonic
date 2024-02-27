import os
import requests
from pytube import YouTube
from pytube.cli import on_progress
from twitterscraper import query_tweets
from TikTokApi import TikTokApi
import instaloader
from bs4 import BeautifulSoup


def youtube_video(video_url, quality='highest'):
    try:
        # Create a YouTube object with the provided video URL
        yt = YouTube(video_url, on_progress_callback=on_progress)

        # Get the stream based on the selected quality
        if quality == 'highest':
            stream = yt.streams.get_highest_resolution()
        elif quality == 'lowest':
            stream = yt.streams.get_lowest_resolution()
        else:
            stream = yt.streams.filter(res=quality).first()

        # Define the save path dynamically based on the operating system
        save_path = os.path.join(os.path.expanduser('~'), 'Downloads')

        # Download the video
        stream.download(output_path=save_path)

        print("\nVideo downloaded successfully!")
    except Exception as e:
        print("\nAn error occurred:", str(e))


def twitter_video(tweet_url, output_file):
    try:
        # Search for tweets containing the given URL
        tweets = query_tweets(f"url:{tweet_url}", limit=1)

        # Check if any tweets were found
        if tweets:
            tweet = tweets[0]

            # Check if the tweet contains a video URL
            if tweet.video_url:
                video_url = tweet.video_url

                os.system(f"wget {video_url} -O {output_file}")

                return True, "Video downloaded successfully!"
            else:
                return False, "No video found in the tweet."
        else:
            return False, "No tweets found containing the URL."
    except Exception as e:
        return False, f"An error occurred: {e}"


def tiktok_video(video_url, output_file):
    try:
        api = TikTokApi()
        video_data = api.get_video_by_url(video_url)
        video_url = video_data['video_url']
        # Download the video using wget or curl
        os.system(f"wget {video_url} -O {output_file}")
        return True, "Video downloaded successfully!"
    except Exception as e:
        return False, f"An error occurred: {e}"


def instagram_video(video_url, output_file):
    try:
        L = instaloader.Instaloader()
        L.download_video(video_url, filename=output_file)
        return True, "Video downloaded successfully!"
    except Exception as e:
        return False, f"An error occurred: {e}"


def facebook_video(post_url):
    response = requests.get(post_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        video_element = soup.find('video')
        if video_element:
            video_url = video_element['src']
            return video_url
    return None
