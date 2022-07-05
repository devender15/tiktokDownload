from django.shortcuts import HttpResponse
from .utils import downloadVideo, getUniqueName, getVideoDownloadLink
from .models import Videos

import os
from pathlib import Path


def downloadTikTok(request):

    video_name = getUniqueName()

    # getting the path of our root directory
    BASE_DIR = Path(__file__).resolve().parent.parent


    if(request.method == 'POST'):
        url = request.POST.get('url')
        
        # getting the download link of the video
        downloadLink = getVideoDownloadLink(url)

        # downloading the video
        downloadVideo(downloadLink, videoName=video_name)

        # pushing the data into the database
        data = Videos(name=video_name, videoUrl=url, videoDownloadUrl=downloadLink)
        data.save()

        # sending back the download response to the client
        with open(os.path.join(str(BASE_DIR) + "/videos", video_name + ".mp4"), "rb") as f:
            data = f.read()

        # download file by response
        response = HttpResponse(data, content_type='application/vnd.mp4')
        response['Content-Disposition'] = f'attachment; filename="{video_name}.mp4"'
        return response
