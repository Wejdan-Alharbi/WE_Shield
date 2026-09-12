import time
import os
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from test_alert_public import send_telegram_alert

WATCH_DIRECTORY = "./monitored_folder"

class FIMHandler(FileSystemEventHandler):
    def get_timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def on_created(self, event):
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            alert_msg = (
                f"🚨 WE_Shield Alert!\n\n"
                f"📌 Event: File Created\n"
                f"📁 File: {file_name}\n"
                f"⏰ Time: {self.get_timestamp()}"
            )
            send_telegram_alert(alert_msg)

    def on_modified(self, event):
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            alert_msg = (
                f"⚠️ WE_Shield Alert!\n\n"
                f"📌 Event: File Modified\n"
                f"📁 File: {file_name}\n"
                f"⏰ Time: {self.get_timestamp()}"
            )
            send_telegram_alert(alert_msg)

    def on_deleted(self, event):
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            alert_msg = (
                f"🗑️ WE_Shield Alert!\n\n"
                f"📌 Event: File Deleted\n"
                f"📁 File: {file_name}\n"
                f"⏰ Time: {self.get_timestamp()}"
            )
            send_telegram_alert(alert_msg)

    def on_moved(self, event):
        if not event.is_directory:
            old_name = os.path.basename(event.src_path)
            new_name = os.path.basename(event.dest_path)
            alert_msg = (
                f"🔄 WE_Shield Alert!\n\n"
                f"📌 Event: File Renamed/Moved\n"
                f"📁 From: {old_name}\n"
                f"➡️ To: {new_name}\n"
                f"⏰ Time: {self.get_timestamp()}"
            )
            send_telegram_alert(alert_msg)

if __name__ == "__main__":
    if not os.path.exists(WATCH_DIRECTORY):
        os.makedirs(WATCH_DIRECTORY)

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
