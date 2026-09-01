import requests

# Public template - Sensitive credentials are kept private for security
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

def send_telegram_alert(message):
    """
    Sends a security alert message to a Telegram chat via Bot API.
    """
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        return {"ok": False, "error": str(e)}

if __name__ == "__main__":
    # Test alert payload for system integration verification
    test_message = (
        "🚨 WE_Shield Alert!\n\n"
        "⚠️ Threat: Test Security Alert\n"
        "📊 Risk Score: 100/100\n"
        "🌐 Status: WE_Shield System Connected Successfully!"
    )
    
    print("WE_Shield Telegram Alert Module Loaded.")
    # Uncomment the following line during local testing with active credentials:
    # print(send_telegram_alert(test_message))
