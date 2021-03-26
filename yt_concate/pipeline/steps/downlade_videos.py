from pytube import YouTube

from .step import Step
from yt_concate.settings import VIDEOS_DIR


class DownladeVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])  # Avoid repeated downloads by use
        print('videos to downldae : ', len(yt_set))

        for yt in yt_set:
            url = yt.url

            # check file have exist or not
            if utils.video_file_exists(yt):
                print(f'find exist file for {url} , skip')
                continue

            print('downlading' + url)
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id)

        return data
