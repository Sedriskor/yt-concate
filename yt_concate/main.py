from yt_concate.pipeline.steps.get_video_list import Get_video_list

from yt_concate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        Get_video_list()
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
