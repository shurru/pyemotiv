import xively
import datetime
import sys
import time
import xml.etree.ElementTree as etree
import numpy

XIVELY_API_KEY= "OXrsK9MwFkcLIJvMRlAouni0TBSYPbT2ZU3tuPpP2uqTZfxi"
XIVELY_FEED_ID= 146826075


# def read_data(stream):
#     for data in stream:
#         if data == '\n':
#             continue
#         try:
#             msg = etree.fromstring(data)
#         except ET.ParseError:
#             print("Error parsing data: '{}'".format(data), end='',file=sys.stderr)
#             continue
#         date = msg.find('./date')
#         hr = int(date.findtext('./hr'))
#         min = int(date.findtext('./min'))
#         sec = int(date.findtext('./sec'))
#         watts = int(msg.findtext('.//watts'))
#         tmpr = float(msg.findtext('./tmpr'))
#         yield datetime.time(hr, min, sec), watts, tmpr


def main():
    api = xively.XivelyAPIClient(XIVELY_API_KEY)
    feed = api.feeds.get(XIVELY_FEED_ID)
    tmpr= numpy.random.randint(4000, 5000)
    watts= numpy.random.randint(0,50)
    now = datetime.datetime.utcnow()
    feed.datastreams = [
        xively.Datastream(id='tmpr', current_value=tmpr, at=now),
        xively.Datastream(id='watts', current_value=watts, at=now),
    ]
    feed.update()
    print(watts, tmpr)


if __name__ == '__main__':
    try:
        args = sys.argv[1:]
        main(*args)
    except KeyboardInterrupt:
        pass