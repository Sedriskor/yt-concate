import sys
import getopt

from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize_yt import InitializeYt
from yt_concate.pipeline.steps.download_caption import DowloadCaptions
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.downlade_videos import DownladeVideos
from yt_concate.pipeline.steps.edit_video import EditVideo
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.utilities import Utils
from yt_concate.pipeline.pipeline import Pipeline


def print_usage():
    print('python3 main.py OPTIONS: ')
    print('--channel_id <channel_id>')
    print('--search_word <word>')
    print('--limit <number>')
    print('--cleanup <True/False>')


def main():
    # CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'
    CHANNEL_ID = 'UCzu_R-RlEXmHUIbfb0GeJDA'  # peko
    WORD = 'ペコ'
    LIMIT = 20

    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': WORD,
        'limit': LIMIT,
        'cleanup': True,
    }

    short_opts = 'hc:s:l:'
    long_opts = 'help channel_id= search_word= limit= cleanup= fast= log='.split()

    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit(0)
        elif opt in ('-c', '--channel_id'):
            inputs['channel_id'] = arg
        elif opt in ('-s', '--search_word'):
            inputs['search_word'] = arg
        elif opt in ('-l', '--limit'):
            inputs['limit'] = int(arg)
        elif opt in ('--cleanup'):
            inputs['cleanup'] = bool(arg)

    print('CHANNEL_ID is ', inputs['channel_id'])
    print('WORD is ', inputs['search_word'])
    print('LIMIT is ', inputs['limit'])
    print('cleanup is ', inputs['cleanup'])

    if not CHANNEL_ID or not WORD:
        print_usage()
        sys.exit(2)

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYt(),
        DowloadCaptions(),
        ReadCaption(),
        Search(),
        DownladeVideos(),
        EditVideo(),
        Postflight()
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
