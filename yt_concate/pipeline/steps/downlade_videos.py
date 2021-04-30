from pytube import YouTube
import time

from .step import Step
from yt_concate.settings import VIDEOS_DIR
from yt_concate.model.log import MyLog

log = MyLog('DownladeVideos')


class DownladeVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])  # Avoid repeated downloads by use

        log.info(f'{len(yt_set)} videos to download ')

        start = time.time()

        for yt in yt_set:
            url = yt.url
            # check file have exist or not
            if utils.video_file_exists(yt):
                log.info(f'find exist file for {url} , skip')
                continue
            log.info(f'downlading: {url}')
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id)

        end = time.time()
        log.info(f'took {end - start} seconds')

        return data
