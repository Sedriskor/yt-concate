from pytube import YouTube
from threading import Thread
import time

from .step import Step
from yt_concate.settings import VIDEOS_DIR


class DownladeVideos(Step):
    # Multithreading
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        print('videos to download', len(yt_set))

        start = time.time()
        threads = []
        for i in range(4):
            threads.append(Thread(target=self.downlade_videos, args=(data[i::4], inputs, utils)))
            # 必須要用 args=() 來做參數傳遞，否則全部跑完才會跳到第二個process
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        end = time.time()
        print('took', end - start, 'seconds')

        return data

    def downlade_videos(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])  # Avoid repeated downloads by use
        for yt in yt_set:
            url = yt.url

            # check file have exist or not
            if utils.video_file_exists(yt):
                print(f'find exist file for {url} , skip')
                continue

            print('downlading: ' + url)
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id)
