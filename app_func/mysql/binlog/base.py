import logging
from queue import Full
from threading import Thread

from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import DeleteRowsEvent, UpdateRowsEvent, WriteRowsEvent

log = logging.getLogger()



class BinlogMonitor(Thread):
    def __init__(self, my_settings, schemas, tables, server_id, name, queue=None, event_maker=None):
        self.my_settings = my_settings
        self.schemas = schemas
        self.tables = tables
        self.name = name
        self.server_id = server_id
        self._q = queue
        self.event_maker = event_maker

    def _start_watching(self):
        stream = BinLogStreamReader(
            connection_settings=self.my_settings,
            server_id=self.server_id,
            blocking=True,
            resume_stream=True,
            only_schemas=self.schemas,
            only_tables=self.tables,
            only_events=[DeleteRowsEvent, UpdateRowsEvent, WriteRowsEvent],
            slave_heartbeat=9
        )

        try:
            for binlog_event in stream:
                for row in binlog_event.rows:
                    if self.event_maker:
                        event = self.event_maker(row)
                    else:
                        event = row

                    if not event:
                        continue
                    if not self._q:
                        log.info(f"no queue to save event {event}")
                        continue

                    try:
                        self._q.put(event)
                    except Full as e:
                        log.info("cmdb event queue full")
                        pass
                    except Exception as e:
                        log.error(f"put event {event} error: {e}")
        finally:
            stream.close()



    def run(self) -> None:
        log.info(f"start binlog moniter {self.name}:")
        try:
            self._start_watching()
        except Exception as e:
            log.error(f"binlog moniter error {e}")
            pass
