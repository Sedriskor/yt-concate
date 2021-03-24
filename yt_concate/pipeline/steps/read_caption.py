import os
from pprint import pprint

from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import CAPTIONS_DIR


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {}  # {caption_file_name : captions}
        for caption_file in os.listdir(CAPTIONS_DIR):
            captions = {}  # {caption : time}
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r', encoding="utf-8") as f:
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

            data[caption_file] = captions
            pprint(data, width=100)  # check ,width=100 pprint width of print
            break

        return data
