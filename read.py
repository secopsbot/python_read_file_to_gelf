#!/usr/bin/env python

from pygelf import GelfTcpHandler, GelfUdpHandler, GelfTlsHandler
import logging
import time
import sys

inFile = sys.argv[1]
inSource = sys.argv[2]


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.addHandler(GelfTcpHandler(host='graylog2.internal', port=12201, compress=False, _logsource=inSource))
#logger.addHandler(GelfUdpHandler(host='graylog2.internal', port=12201, debug=True, chunk_size=1350))


import time

buffsize = 0

with open(inFile) as f1:
    lines = f1.readlines()
    for i, line in enumerate(lines):
            logging.info(line)
#            time.sleep( 1 )
