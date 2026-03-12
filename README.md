# 🔐 Tamper-Proof Chat Logging System

A simple educational project demonstrating tamper-proof logging using **cryptographic hash chaining (SHA-256)**.  
The system simulates a chat application with secure logs, where any modification to stored logs is automatically detected.

**Built using:** Python · Streamlit · SHA-256 Cryptographic Hashing

---

## 🌐 Live Application

Try the hosted app here:

👉 **Streamlit App:** [https://tamper-proof-chat-app.streamlit.app/](https://tamper-proof-chat-app.streamlit.app/)

---

## 📚 Project Documentation

Full explanation of the system architecture, mathematics, and implementation:

👉 **Documentation Page:** [https://priyanshu-rajsingh.github.io/tamper-proof-chat-streamlit/](https://priyanshu-rajsingh.github.io/tamper-proof-chat-streamlit/)

---

## 🚀 Quick Start (Local Setup)

**1. Clone the repository:**
```bash
git clone https://github.com/Priyanshu-rajsingh/tamper-proof-chat-streamlit.git
```

**2. Navigate to the project folder:**
```bash
cd tamper-proof-chat-streamlit
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Run the application:**
```bash
streamlit run app.py
```

**5. Open in browser:**
```
http://localhost:8501
```

---

## 🔎 Features

| Feature | Description |
|---|---|
| 💬 Chat Simulation | Simulated two-user chat system |
| 🔗 Hash Chaining | Tamper-proof log storage using SHA-256 |
| 🛠 Admin Panel | Monitor and verify log integrity |
| ⚠ Tampering Simulation | Manually modify logs to trigger detection |
| 🎨 Visualization | Visual hash-chain representation |
| 📖 Educational | Clear explanation of the security concept |

---

## 🧠 Security Concept

Each log entry stores the hash of the previous log:
```
Hᵢ = SHA256(Mᵢ || Tᵢ || Hᵢ₋₁)
```

This creates a chain of hashes:
```
Log0 ──► Log1 ──► Log2 ──► Log3
```

If any message is modified, the hash chain breaks and tampering is automatically detected.

---

## 👨‍💻 Author

**Priyanshu Raj Singh**  
Computer Science Engineering Student · Cybersecurity & Systems Enthusiast
