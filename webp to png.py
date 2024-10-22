import time, os, glob
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image

class WebPHandler(FileSystemEventHandler):
    def __init__(self, folder):
        self.folder = folder
        self.convert_existing_files()
        self.processing = set()

    def convert_existing_files(self):
        for webp in glob.glob(os.path.join(self.folder, "*.webp")):
            self.convert_file(webp)

    def on_created(self, event):
        if event.src_path.endswith(".webp"):
            self.convert_file(event.src_path)

    def on_modified(self, event):
        if event.src_path.endswith(".webp"):
            self.convert_file(event.src_path)

    def convert_file(self, webp_file):
        if webp_file in self.processing:
            return
        self.processing.add(webp_file)
        time.sleep(1)  # Wait for file to be ready
        try:
            if os.path.exists(webp_file) and os.path.getsize(webp_file):
                png_file = webp_file.replace(".webp", ".png")
                Image.open(webp_file).save(png_file, "PNG")
                os.remove(webp_file)
                print(f"Converted: {os.path.basename(webp_file)}")
        except Exception as e:
            print(f"Error converting {os.path.basename(webp_file)}: {e}")
        finally:
            self.processing.remove(webp_file)

if __name__ == "__main__":
    folder = r"C:\Users\Smitm\Downloads"
    handler = WebPHandler(folder)
    observer = Observer()
    observer.schedule(handler, folder, recursive=False)
    observer.start()
    print(f"Monitoring: {folder}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()