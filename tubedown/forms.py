from django import forms


class YoutubeVideoForm(forms.Form):
    video_url = forms.URLField(label='', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Enter video URL', 'type': 'url', 'id': 'video-url'}))
    quality = forms.ChoiceField(label='', choices=[(
        'highest', 'Highest'), ('lowest', 'Lowest')], required=True, widget=forms.Select(attrs={'class': 'custom-select'}))


class TwitterVideoForm(forms.Form):
    tweet_url = forms.URLField(label='', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Enter Tweet URL', 'type': 'url', 'id': 'tweet-url'}))


class TikTokForm(forms.Form):
    tiktok_url = forms.URLField(label='', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Enter TikTok Video URL', 'type': 'url', 'id': 'tiktok-url'}))


class InstagramForm(forms.Form):
    instagram_url = forms.URLField(label='', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Enter Instagram Video URL', 'type': 'url', 'id': 'instagram-url'}))


class FacebookForm(forms.Form):
    facebook_url = forms.URLField(label='', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Enter Facebook Video URL', 'type': 'url', 'id': 'facebook-url'}))
