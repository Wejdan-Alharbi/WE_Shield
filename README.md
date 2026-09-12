# WE_Shield - File Integrity Monitoring System (FIM)

WE_Shield is a lightweight, real-time File Integrity Monitoring (FIM) agent written in Python. It continuously monitors target directories for file integrity events, calculates cryptographic hashes to detect actual content tampering, and dispatches detailed security alerts via Telegram.

---

## Key Features
- **Cryptographic Hash Verification**: Utilizes SHA-256 hashing algorithm to verify file integrity and prevent false positive alerts.
- **Comprehensive Event Monitoring**: Real-time tracking of creation, modification, deletion, and renaming/moving of files.
- **Detailed Telegram Alerts**: Instant security notifications including exact timestamps, event types, and SHA-256 hash snippets.
- **Secure Credential Isolation**: Implements security best practices by completely separating sensitive Telegram credentials from core application logic.
- **Lightweight Execution**: Optimized file system auditing with minimal system resource consumption.

---

## Tech Stack
- Python 3.x
- hashlib (SHA-256 Integrity Engine)
- watchdog (File System Event Monitoring)
- requests (Telegram Alert Dispatcher)
