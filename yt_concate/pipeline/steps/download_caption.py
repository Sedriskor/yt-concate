from pytube import YouTube
from threading import Thread
import time

from yt_concate.pipeline.steps.step import Step
from yt_concate.model.log import MyLog

log = MyLog('DowloadCaptions')

class DowloadCaptions(Step):
    # Multithreading
    def process(self, data, inputs, utils):

        start = time.time()
        threads = []
        for i in range(4):
            threads.append(Thread(target=self.download_caption, args=(data[i::4], inputs, utils)))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        end = time.time()
        log.info(f'took{end - start}seconds')

        return data

    def download_caption(self, data, inputs, utils):
        for yt in data:
            # check file have exist or not
            log.info(f'downloading caption for {yt.id}')
            if utils.caption_file_exists(yt):
                log.info('find exist file')
                continue

            # main function
            try:
                source = YouTube(yt.url)
                yt_caption = source.captions.get_by_language_code('a.ja')
                yt_caption_convert_to_srt = yt_caption.generate_srt_captions()

            except (KeyError, AttributeError):
                log.error(f'when downloading caption {yt.url}')
                continue

            # save the caption to a file named Output.txt
            text_file = open(yt.caption_filepath, "w", encoding="utf-8")
            text_file.write(yt_caption_convert_to_srt)
            text_file.close()
