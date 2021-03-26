from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize_yt import InitializeYt
from yt_concate.pipeline.steps.download_caption import DowloadCaptions
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.downlade_videos import DownladeVideos
from yt_concate.pipeline.steps.postflight import Postflight

# from yt_concate.pipeline.steps.stp import StepException
from yt_concate.utilities import Utils

from yt_concate.pipeline.pipeline import Pipeline

# CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'
CHANNEL_ID = 'UCzu_R-RlEXmHUIbfb0GeJDA'  # peko


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'ペコ',
    }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYt(),
        DowloadCaptions(),
        ReadCaption(),
        Search(),
        DownladeVideos(),
        Postflight()
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
