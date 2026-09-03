import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from test_alert_public import send_telegram_alert

# Directory to monitor
WATCH_DIRECTORY = "./monitored_folder"

class FIMHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            alert_msg = f"⚠️ WE_Shield Alert!\n\n🚨 Event: File Modified\n📁 File: {file_name}"
            send_telegram_alert(alert_msg)

    def on_created(self, event):
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            alert_msg = f"⚠️ WE_Shield Alert!\n\n🆕 Event: File Created\n📁 File: {file_name}"
            send_telegram_alert(alert_msg)

if __name__ == "__main__":
    if not os.path.exists(WATCH_DIRECTORY):
        os.makedirs(WATCH_DIRECTORY)
        print(f"[*] Created directory to monitor: {WATCH_DIRECTORY}")

    event_handler = FIMHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_DIRECTORY, recursive=False)
    observer.start()

    print(f"🛡️ WE_Shield FIM Engine Running... Monitoring: {WATCH_DIRECTORY}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n[!] Stopping WE_Shield Monitor...")
    observer.join()
