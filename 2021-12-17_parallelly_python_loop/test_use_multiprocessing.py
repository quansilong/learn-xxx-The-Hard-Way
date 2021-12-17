#!/usr/bin/env python3

import time, logging
from multiprocessing.dummy import Pool as ThreadPool

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s [%(levelname)s] %(message)s')
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger

def process(item):
    log = get_logger(item)
    log.info("item: {}".format(item))
    time.sleep(1)

items = ['apple', 'bananan', 'cake', 'dumpling']

# serial performing
# for item in items:
#     process(item)

#print("\n", "="*32, "\n")
# parallel performing
pool = ThreadPool()
pool.map(process, items)
pool.close()
pool.join()