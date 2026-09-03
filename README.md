# WE_Shield - File Integrity Monitoring System (FIM)

WE_Shield is a lightweight, real-time File Integrity Monitoring (FIM) agent written in Python. It continuously monitors target directories for file creation or modification events and instantly dispatches security alerts via Telegram.

---

## Key Features
- Real-Time Event Monitoring: Utilizes system-level event hooks for minimal latency using watchdog.
- Automated Telegram Alerts: Instant security notifications dispatched straight to Telegram channels via Telegram Bot API.
- Secure Credential Isolation: Built with operational security best practices, ensuring API tokens and Chat IDs are handled safely.
- Lightweight & Efficient: Runs seamlessly in the background with minimal system resource consumption.

---

## Tech Stack
- Python 3.x
- watchdog
- requests
