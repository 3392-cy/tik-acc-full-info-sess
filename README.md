# TikTok Full Info Session 🔐
**by @gqpgqpg**

A Python tool that extracts **full TikTok account information directly from a valid session ID**, including **general account details, security bindings, and wallet / balance data**.

This tool works **only with a valid logged-in TikTok session** and provides information that is **not accessible via public profiles**.

---

## ✨ Features

### 👤 General Account Information
- Username
- User ID & Sec User ID
- Screen name
- Profile picture URL
- Bio / description
- Account creation date
- Connected login methods
- Session key
- Employee / internal account flags
- External employee platform detection
- Email & mobile binding (if available)

### 💰 Wallet & Balance Information
- Coin balance
- Frozen coins
- Recharge availability
- Google recharge support
- Quick payment availability
- PC web recharge status
- Periodic payout eligibility
- Email confirmation status
- Redeem & payout metadata
- Web recharge input options
- Payment method availability indicator

---

## 🧠 How It Works

This tool uses:
- **Authenticated web endpoints**
- A **valid `sessionid` cookie**
- TikTok wallet & passport APIs

No signing is required — authentication relies entirely on the provided session.

---

## 📦 Requirements

- Python **3.8+**
- Dependencies:
  ```bash
  pip install requests
