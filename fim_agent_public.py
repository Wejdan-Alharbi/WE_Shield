import time
import os
import hashlib
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from test_alert_public import send_telegram_alert

WATCH_DIRECTORY = "./monitored_folder"

# Dictionary to store file SHA-256 hashes
file_hashes = {}

def calculate_sha256(filepath):
    """Calculates SHA-256 hash for a given file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception:
        return None

class FIMHandler(FileSystemEventHandler):
    def get_timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def on_created(self, event):
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            time.sleep(0.1)
            file_hash = calculate_sha256(event.src_path)
            
            if file_hash:
                file_hashes[event.src_path] = file_hash
            
            short_hash = file_hash[:12] if file_hash else "N/A"
            
            alert_msg = (
                f"🚨 WE_Shield Alert!\n\n"
                f"📌 Event: File Created\n"
                f"📁 File: {file_name}\n"
                f"🔑 SHA-256: {short_hash}...\n"
                f"⏰ Time: {self.get_timestamp()}"
            )
            send_telegram_alert(alert_msg)

    def on_modified(self, event):
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            time.sleep(0.1)
            new_hash = calculate_sha256(event.src_path)
            
            if not new_hash:
                return

            old_hash = file_hashes.get(event.src_path)

            # Check if actual content changed to avoid false positives
            if old_hash != new_hash:
                file_hashes[event.src_path] = new_hash
                short_hash = new_hash[:12]
                
                alert_msg = (
                    f"⚠️ WE_Shield Alert!\n\n"
                    f"📌 Event: File Modified (Integrity Changed)\n"
                    f"📁 File: {file_name}\n"
                    f"🔑 New SHA-256: {short_hash}...\n"
                    f"⏰ Time: {self.get_timestamp()}"
                )
                send_telegram_alert(alert_msg)

    def on_deleted(self, event):
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            if event.src_path in file_hashes:
                del file_hashes[event.src_path]
                
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
            
            if event.src_path in file_hashes:
                file_hashes[event.dest_path] = file_hashes.pop(event.src_path)
                
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

    # Initial hashing of existing files in the directory
    for root, dirs, files in os.walk(WATCH_DIRECTORY):
        for file in files:
            full_path = os.path.join(root, file)
            file_hashes[full_path] = calculate_sha256(full_path)

    event_handler = FIMHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_DIRECTORY, recursive=False)
    observer.start()

    print(f"🛡️ WE_Shield FIM Engine (SHA-256 Integrity Active)... Monitoring: {WATCH_DIRECTORY}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n[!] Stopping WE_Shield Monitor...")
    observer.join()
