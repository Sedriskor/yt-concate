from .step import Step
from yt_concate.settings import OUTPUT_DIR
from yt_concate.model.log import MyLog

log = MyLog('Postflight')

import os


class Postflight(Step):
    def process(self, data, inputs, utils):
        log.info('in Postflight')

        if inputs['cleanup'] == True:
            if len(os.listdir(OUTPUT_DIR)) > 0:
                log.info('found existing output file')
                log.info('delete downloaded file')
                utils.remove_dirs()
            else:
                pass
