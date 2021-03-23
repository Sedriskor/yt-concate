from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.download_caption import DowloadCaptions
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.postflight import Postflight

# from yt_concate.pipeline.steps.stp import StepException
from yt_concate.utilities import Utils

from yt_concate.pipeline.pipeline import Pipeline

# CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'
CHANNEL_ID = 'UCzu_R-RlEXmHUIbfb0GeJDA'  # peko


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        Preflight(),
        GetVideoList(),
        DowloadCaptions(),
        Postflight()
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
