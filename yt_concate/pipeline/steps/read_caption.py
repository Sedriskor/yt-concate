from pprint import pprint

from yt_concate.pipeline.steps.step import Step


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            # check if no caption file for id
            if not utils.caption_file_exists(yt):
                continue

            captions = {}
            with open(yt.caption_filepath, 'r', encoding="utf-8") as f:
                time_line = False
                for line in f:
                    if '-->' in line:
                        time_line = True
                        time = line.strip()
                        continue
                    if time_line:
                        caption = line.strip()
                        captions[caption] = time
                        time_line = False

            yt.captions = captions
            # pprint(captions, width=100)  # check ,width=100 pprint width of print

        return data
