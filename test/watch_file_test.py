
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

BASEDIR = os.path.abspath(os.path.dirname(__file__))

def getext(filename):
    return os.path.splitext(filename)[-1].lower()

class ChangeHandler(FileSystemEventHandler):

    def on_modified(self, event):
        if event.is_directory:
            return
        if getext(event.src_path) in ('test.txt'):
            os.system('python read_test.py')
            #print('%s has been modified.' % event.src_path)

if __name__ in '__main__':
    while 1:
        event_handler = ChangeHandler()
        observer = Observer()
        observer.schedule(event_handler,BASEDIR,recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
