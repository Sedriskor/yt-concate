from pytube import YouTube

from yt_concate.pipeline.steps.step import Step


# from yt_concate.pipeline.steps.step import StepException

class DowloadCaptions(Step):
    def process(self, data, inputs, utils):
        for url in data:

            print('downloading caption for', url)  # check
            if utils.caption_file_exists(url):
                print('find exist file')
                continue

            try:
                source = YouTube(url)
                print(source.captions)  # check
                yt_caption = source.captions.get_by_language_code('a.ja')
                yt_caption_convert_to_srt = (yt_caption.generate_srt_captions())

            except (KeyError, AttributeError):
                print('Error when downloading caption', url)
                continue

            # save the caption to a file named Output.txt
            text_file = open(utils.get_caption_filepath(url), "w", encoding="utf-8")
            text_file.write(yt_caption_convert_to_srt)
            text_file.close()
            break
