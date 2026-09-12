# WE_Shield - File Integrity Monitoring System (FIM)

WE_Shield is a lightweight, real-time File Integrity Monitoring (FIM) agent written in Python. It continuously monitors target directories for file integrity events and instantly dispatches detailed security alerts via Telegram.

---

## Key Features
- Comprehensive Event Monitoring: Tracks creation, modification, deletion, and renaming/moving of files in real time.
- Detailed Telegram Alerts: Delivers immediate security notifications with structured event types and exact timestamps.
- Secure Credential Isolation: Built with operational security best practices to isolate API tokens and Chat IDs.
- Lightweight & Efficient: Runs seamlessly in the background using system-level event hooks with minimal resource overhead.

---

## Tech Stack
- Python 3.x
- watchdog
- requests
