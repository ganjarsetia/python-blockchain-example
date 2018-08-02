import time
import sys
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from subprocess import call


class MyHandler(LoggingEventHandler):
    patterns = ["*.py"]

    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        # the file will be processed there
        # print(event.src_path, event.event_type)
        call(["python3", "./test.py"])

    """ def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event) """

    def on_any_event(self, event):
        self.process(event)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    call(["python3", "./test.py"])
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(MyHandler(), path=(args[0] if args else '.'))
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
