import os
# import json
# from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import *
from .utils import *
from http.client import IncompleteRead
 

def index(request):
    if request.method == 'POST':
        if 'twitter_submit' in request.POST:
            form = TwitterVideoForm(request.POST)
            if form.is_valid():
                tweet_url = form.cleaned_data['tweet_url']
                filename = os.path.basename(video_url)
                output_file = os.path.join(tweet_url, filename)
                success, message = twitter_video(tweet_url, output_file)
                return redirect('twitter')
        elif 'tiktok_submit' in request.POST:
            form = TikTokForm(request.POST)
            if form.is_valid():
                video_url = form.cleaned_data['tiktok_url']
                filename = os.path.basename(video_url)
                output_file = os.path.join(video_url, filename)
                success, message = tiktok_video(video_url, output_file)
                return redirect('tiktok')
        elif 'youtube_submit' in request.POST:
            form = YoutubeVideoForm(request.POST)
            if form.is_valid():
                video_url = form.cleaned_data['video_url']
                quality = form.cleaned_data['quality']
                try:
                    youtube_video(video_url, quality)
                    messages.success(request, 'Video downloaded successfully!')
                except IncompleteRead:
                    messages.error(
                        request, 'An error occurred: The download was incomplete. Due to Network Error. Please try again later.')
                except Exception as e:
                    messages.error(request, f'An error occurred: {str(e)}')
                return redirect('youtube')
        elif 'instagram_submit' in request.POST:
            form = InstagramForm(request.POST)
            if form.is_valid():
                video_url = form.cleaned_data['instagram_url']
                filename = os.path.basename(video_url)
                output_file = os.path.join(video_url, filename)
                success, message = instagram_video(video_url, output_file)
                return redirect('instagram')
        elif 'facebook_submit' in request.POST:
            form = FacebookForm(request.POST)
            if form.is_valid():
                post_url = form.cleaned_data['post_url']
                video_url = facebook_video(post_url)
                filename = os.path.basename(video_url)
                output_file = os.path.join(video_url, filename)
                success, message = facebook_video(post_url, output_file)
                return redirect('facebook')
    else:
        tiktok_form = TikTokForm()
        instagram_form = InstagramForm()
        facebook_form = FacebookForm()
        youtube_form = YoutubeVideoForm()
        twitter_form = TwitterVideoForm()
    return render(request, 'index.html', {'tiktok_form': tiktok_form, 'instagram_form': instagram_form, 'facebook_form': facebook_form, 'youtube_form': youtube_form, 'twitter_form': twitter_form, 'message': None})


def youtube(request):
    if request.method == 'POST':
        form = YoutubeVideoForm(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data['video_url']
            quality = form.cleaned_data['quality']
            try:
                youtube_video(video_url, quality)
                messages.success(request, 'Video downloaded successfully!')
            except IncompleteRead:
                messages.error(
                    request, 'An error occurred: The download was incomplete. Due to Network Error. Please try again later.')
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
            return redirect('youtube')
    else:
        youtube_form = YoutubeVideoForm()
    return render(request, 'youtube.html', {'youtube_form': youtube_form})


def twitter(request):
    if request.method == 'POST':
        form = TwitterVideoForm(request.POST)
        if form.is_valid():
            tweet_url = form.cleaned_data['tweet_url']
            filename = os.path.basename(tweet_url)
            output_file = os.path.join(tweet_url, filename)
            success, message = twitter_video(tweet_url, output_file)
            return redirect('twitter')
    else:
        twitter_form = TwitterVideoForm()
    return render(request, 'twitter.html', {'twitter_form': twitter_form, 'message': None})


def tiktok(request):
    if request.method == 'POST':
        form = TikTokForm(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data['tiktok_url']
            filename = os.path.basename(video_url)
            output_file = os.path.join(video_url, filename)
            success, message = tiktok_video(video_url, output_file)
            return redirect('tiktok')
    else:
        tiktok_form = TikTokForm()
    return render(request, 'tiktok.html', {'tiktok_form': tiktok_form, 'message': None})


def instagram(request):
    if request.method == 'POST':
        form = InstagramForm(request.POST)
        if form.is_valid():
            print("hjggki")
            
            video_url = form.cleaned_data['instagram_url']
            filename = os.path.basename(video_url)
            output_file = os.path.join(video_url, filename)
            success, message = instagram_video(video_url, output_file)
            return redirect('instagram')
    else:
        instagram_form = InstagramForm()
    return render(request, 'instagram.html', {'instagram_form': instagram_form, 'message': None})


def facebook(request):
    if request.method == 'POST':
        form = FacebookForm(request.POST)
        if form.is_valid():
            post_url = form.cleaned_data['post_url']
            video_url = facebook_video(post_url)
            filename = os.path.basename(video_url)
            output_file = os.path.join(video_url, filename)
            success, message = facebook_video(post_url, output_file)
            return redirect('facebook')
    else:
        facebook_form = FacebookForm()
    return render(request, 'facebook.html', {'facebook_form': facebook_form, 'message': None})
