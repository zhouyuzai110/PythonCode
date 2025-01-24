import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):

    def on_modified(self, event):
        print(f'File {event.src_path} has been modified')

    def on_moved(self, event):
        print(f'File {event.src_path} has been moved to {event.dest_path}')

    def on_created(self, event):
        print(f'File {event.src_path} has been created')

    def on_deleted(self, event):
        print(f'File {event.src_path} has been deleted')


if __name__ == "__main__":
    path_to_watch = r"F:\vitepress\docs"  # 包含子目录的路径

    event_handler = MyHandler()
    observer = Observer()

    # 设置为递归监控，包括子目录中的所有变化
    observer.schedule(event_handler, path=path_to_watch, recursive=True)

    observer.start()

    try:
        while True:
            time.sleep(1)  # 保持主程序运行，以便观察者可以持续监听
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
