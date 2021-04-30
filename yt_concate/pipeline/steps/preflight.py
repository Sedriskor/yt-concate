from .step import Step
from yt_concate.model.log import MyLog

log = MyLog('Preflight')

class Preflight(Step):
    def process(self, data, inputs, utils):

        log.info('in Preflight')
        utils.create_dir()
