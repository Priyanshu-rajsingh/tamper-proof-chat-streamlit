
🔐 Tamper-Proof Chat Logging System
A secure chat logging system that demonstrates tamper-proof logging using cryptographic hash chaining. This project simulates a secure audit log where any unauthorized modification is automatically detected — serving as an educational demonstration of integrity protection in cybersecurity systems.
Tech Stack: Python · Streamlit · SHA-256 · JSON

📚 Table of Contents

Introduction
Problem Statement
Security Objectives
System Architecture
Cryptographic Background
Mathematical Model
Tampering Detection
Application Workflow
Installation & Setup
Running the Project
Demonstration Scenario
Real-World Applications
Future Improvements


1. Introduction
Modern information systems rely heavily on log files to record activities such as user logins, financial transactions, system events, and security alerts. However, attackers who gain system access may attempt to modify these logs to conceal their actions.
This project demonstrates a tamper-proof logging mechanism using cryptographic hash chaining — a technique similar to those used in:

Blockchain systems
Secure audit trails
Financial record systems
Cybersecurity monitoring platforms


2. Problem Statement
Traditional logging systems store records sequentially with no built-in integrity protection:
Log1 → Log2 → Log3 → Log4
An attacker can easily modify these records without detection. For example:
Log EntryOriginalUserA: Login successfulTamperedUserA: No activity
There is no mechanism to detect such changes in a conventional logging system.

3. Security Objectives
This system is designed to achieve three core security properties:
PropertyDescriptionIntegrityLog entries cannot be modified without detectionTraceabilityEvery log entry is cryptographically linked to the previous oneTamper DetectionAny modification invalidates the entire hash chain

4. System Architecture
Users
  │  (Chat Messages)
  ▼
Streamlit Web Application
  │
  ▼
Hash Chain Logging System
  │
  ▼
logs.json  (Persistent Storage)
  │
  ▼
Admin Verification Panel
The admin panel allows verification of the full log chain's integrity at any time.

5. Cryptographic Background
This project uses the SHA-256 cryptographic hash function, which has the following properties:
PropertyDescriptionDeterministicSame input always produces the same outputCollision ResistantExtremely difficult to produce the same hash from two different inputsPreimage ResistantCannot reconstruct the original input from its hashAvalanche EffectA small change in input produces a completely different hash
Example — even a tiny change produces a completely different hash:
Input:  "Hello"
SHA256: 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969

Input:  "Hello!"
SHA256: 334d016f755cd6dc58c53a86e183882f8ec14f52fb05345887c8a5edd42c87b7

6. Mathematical Model of Hash Chaining
Let:

Mᵢ = the message of log entry i
Tᵢ = the timestamp of log entry i
Hᵢ₋₁ = the hash of the previous log entry

The hash of each log entry is defined as:
Hᵢ = SHA256(Mᵢ || Tᵢ || Hᵢ₋₁)
where || denotes concatenation. The first entry uses 0 as its previous hash:
H₀ = SHA256(M₀ || T₀ || 0)
H₁ = SHA256(M₁ || T₁ || H₀)
H₂ = SHA256(M₂ || T₂ || H₁)
This creates a chain where each entry depends on all previous entries:
Log0 ──H₀──▶ Log1 ──H₁──▶ Log2 ──H₂──▶ Log3

7. Tampering Detection
If an attacker modifies any message in the chain:
Original:  "UserB: Hi"
Tampered:  "UserB: Send OTP"
The recalculated hash Hᵢ' will not match the stored hash Hᵢ, causing a chain break:
Hᵢ' ≠ Hᵢ  →  ⚠️ Tampering Detected
Because every subsequent hash depends on the modified entry, the entire downstream chain is invalidated — making silent tampering impossible.

8. Application Workflow
Step 1  →  User sends a message (e.g., "UserA: Hello")
Step 2  →  System creates a log entry: { message, timestamp, prevHash, hash }
Step 3  →  New log is appended to the chain
Step 4  →  Admin triggers verification — all hashes are recomputed
              ✅ Stored Hash == Recomputed Hash  →  Logs are VALID
              ❌ Mismatch detected               →  Tampering Detected

9. Installation & Setup
Step 1 — Clone the repository:
bashgit clone https://github.com/Priyanshu-rajsingh/tamper-proof-chat-streamlit.git
cd tamper-proof-chat-streamlit
Step 2 — Install dependencies:
bashpip install -r requirements.txt
Or manually:
bashpip install streamlit

10. Running the Project
bashstreamlit run app.py
```

Then open your browser and navigate to:
```
http://localhost:8501

11. Demonstration Scenario

Users send messages — e.g., UserA: Hello, UserB: Hi
Admin opens the log panel — status shows: ✅ Logs are VALID
Admin simulates tampering — modifies a log entry (e.g., changes "Hi" to "Send OTP")
System re-verifies the chain — result: ❌ Tampering Detected


12. Real-World Applications
Hash-chained logging is used across many security-critical domains:
DomainUse CaseBlockchainEnsures immutability of transaction recordsFinancial SystemsProtects banking and transaction audit logsSecurity MonitoringPrevents attackers from hiding their tracesDigital ForensicsMaintains trustworthy evidence recordsAudit & ComplianceEnsures regulatory compliance through verifiable logs

13. Future Improvements

Real-time multi-user chat using WebSockets
Digital signatures for stronger log authentication
Distributed logging using blockchain
Database storage to replace JSON files
Automated intrusion alerts on tampering detection
Visual hash chain graph for intuitive exploration


This project is provided for educational and research purposes.
