# WE_Shield - File Integrity Monitoring System (FIM) 🛡️

**WE_Shield** is a lightweight, real-time File Integrity Monitoring (FIM) agent written in Python. It continuously audits target directories for file events, calculates SHA-256 cryptographic hashes to detect actual content tampering, and dispatches real-time security alerts via Telegram.

---

## 🔑 Key Features
- **SHA-256 Integrity Verification**: Calculates cryptographic hashes to confirm content modification and eliminate false positives.
- **Real-Time Event Auditing**: Detects file creation, modification, deletion, and renaming/moving events instantly.
- **Automated Telegram Notifications**: Sends structured security alerts containing event types, timestamps, and hash signatures.
- **Secure Architecture**: Enforces strict credential isolation between application logic and private API keys.

---

## 🛠️ Tech Stack
- **Language**: Python 3.x
- **Core Libraries**: `hashlib` (Cryptographic Engine), `watchdog` (File System Auditor), `requests` (API Dispatcher)

---

## 📁 Project Structure
```plaintext
WE_Shield/
├── fim_agent_public.py       # Core FIM auditing logic
├── test_alert_public.py     # Public alert module template
├── .gitignore               # Excluded local & private files
└── README.md                # Project documentation

## 🚀 How to Run Locally

1. Clone the Repository:
git clone https://github.com/Wejdan-Alharbi/WE_Shield.git
cd WE_Shield

2. Install Dependencies:
pip install watchdog requests

3. Configure Credentials:
- Create a local file named test_alert.py
- Add your Telegram BOT_TOKEN and CHAT_ID

4. Start the FIM Engine:
python fim_agent_public.py
