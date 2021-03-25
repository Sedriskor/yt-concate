from pytube import YouTube

from yt_concate.pipeline.steps.step import Step


# from yt_concate.pipeline.steps.step import StepException

class DowloadCaptions(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            # check file have exist or not
            print('downloading caption for', yt.id)
            if utils.caption_file_exists(yt):
                print('find exist file')
                continue

            # main function
            try:
                source = YouTube(yt.url)
                yt_caption = source.captions.get_by_language_code('a.ja')
                yt_caption_convert_to_srt = (yt_caption.generate_srt_captions())

            except (KeyError, AttributeError):
                print('Error when downloading caption', yt.url)
                continue

            # save the caption to a file named Output.txt
            text_file = open(utils.get_caption_filepath(yt.url), "w", encoding="utf-8")
            text_file.write(yt_caption_convert_to_srt)
            text_file.close()

        return data
