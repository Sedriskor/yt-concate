from .step import Step
from yt_concate.settings import OUTPUT_DIR

import os

class Postflight(Step):
    def process(self, data, inputs, utils):
        print('in Postflight')

        if inputs['cleanup'] == True:
            if len(os.listdir(OUTPUT_DIR)) > 0 :
                print('found existing output file')
                print('delete downloaded file')
                utils.remove_dirs()
            else:
                pass