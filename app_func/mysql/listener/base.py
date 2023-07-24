import logging
from queue import Empty, Queue
from threading import Thread

log = logging.getLogger()


class Listener(Thread):
    def __init__(self, q:Queue, name, operator):
        self._q = q
        self.name = name
        self.operator = operator

    def run(self) -> None:
        log.info(f"start listener {self.name}")
        try:
            while True:
                try:
                    event = self._q.get(timeout=5)
                    log.info(f"listener get event {event} from queue")
                    self.operator.work(event)
                except Empty:
                    pass
                except Exception as e:
                    log.error(f"listener get event error: {e}")
                    import traceback
                    log.error(traceback.format_exc())
        except Exception as e:
            log.error(f"listener work error: {e}")
            pass
