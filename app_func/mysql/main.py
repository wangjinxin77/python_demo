import logging
from queue import Queue

from const import MYSQL_SETTINGS
from binlog.base import BinlogMonitor
from listener.base import Listener

log = logging.getLogger()


class Operator(object):
    @staticmethod
    def work(event):
        log.info(f"Operator work event {event}")
        pass


def main():
    q = Queue()
    binlog = BinlogMonitor(MYSQL_SETTINGS, ["nsp-o"], ["region"], 99, "test_binlog", q)
    operator = Operator()
    listener = Listener(q, "my_listener", operator)
    binlog.start()
    listener.start()


if __name__ == "__main__":
    main()
