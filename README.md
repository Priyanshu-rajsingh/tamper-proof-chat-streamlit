# tamper-proof-chat-app

🔐 Tamper-Proof Chat Logging System using Hash Chaining

A secure chat logging system that demonstrates tamper-proof logging using cryptographic hash chaining.
This project simulates a secure audit log system where any unauthorized modification of logs is automatically detected.

The application is implemented using Python + Streamlit and is designed as an educational demonstration of integrity protection in cybersecurity systems.

📚 Table of Contents

Introduction

Problem Statement

Security Objectives

System Architecture

Cryptographic Background

Mathematical Model of Hash Chaining

Tampering Detection Mechanism

Application Workflow

Installation and Setup

Running the Project

Demonstration Scenario

Real-World Applications

Future Improvements

1️⃣ Introduction

Modern information systems rely heavily on log files to record activities such as:

user logins

financial transactions

system events

security alerts

However, attackers who gain system access may attempt to modify logs to hide their actions.

Therefore, it is critical to ensure log integrity.

This project demonstrates a tamper-proof logging mechanism using cryptographic hash chaining, similar to techniques used in:

blockchain systems

secure audit trails

financial record systems

cybersecurity monitoring platforms

2️⃣ Problem Statement

Traditional logging systems store records sequentially:

Log1
Log2
Log3
Log4

An attacker can easily modify these records.

Example attack:

Original Log
UserA: Login successful

Tampered Log
UserA: No activity

There is no built-in mechanism to detect such changes.

3️⃣ Security Objectives

This system aims to achieve the following security properties:

Integrity

Ensure that log entries cannot be modified without detection.

Traceability

Every log entry is linked to the previous log.

Tamper Detection

Any modification of a log entry will invalidate the entire hash chain.

4️⃣ System Architecture
Users
  │
  │ Chat Messages
  ▼
Streamlit Web Application
  │
  │
Hash Chain Logging System
  │
  ▼
logs.json (Persistent Storage)
  │
  ▼
Admin Verification Panel

The admin panel verifies the integrity of the log chain.

5️⃣ Cryptographic Background

This project uses the SHA-256 cryptographic hash function.

SHA-256 Properties
Property	Description
Deterministic	Same input produces same output
Collision Resistant	Extremely difficult to produce same hash from different inputs
Preimage Resistant	Cannot reconstruct input from hash
Avalanche Effect	Small change in input produces large change in hash

Example:

Input
Hello

SHA256
185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969

Even a small change:

Hello!

Produces a completely different hash.

6️⃣ Mathematical Model of Hash Chaining

Let:

𝑀
𝑖
M
i
	​

 be the message of log entry 
𝑖
i

𝑇
𝑖
T
i
	​

 be the timestamp

𝐻
𝑖
−
1
H
i−1
	​

 be the previous hash

The hash of the current log entry is defined as:

𝐻
𝑖
=
𝑆
𝐻
𝐴
256
(
𝑀
𝑖
  
∣
∣
  
𝑇
𝑖
  
∣
∣
  
𝐻
𝑖
−
1
)
H
i
	​

=SHA256(M
i
	​

∣∣T
i
	​

∣∣H
i−1
	​

)

Where:

∣
∣
∣∣ represents concatenation

Hash Chain Structure
𝐻
0
=
𝑆
𝐻
𝐴
256
(
𝑀
0
∣
∣
𝑇
0
∣
∣
0
)
H
0
	​

=SHA256(M
0
	​

∣∣T
0
	​

∣∣0)
𝐻
1
=
𝑆
𝐻
𝐴
256
(
𝑀
1
∣
∣
𝑇
1
∣
∣
𝐻
0
)
H
1
	​

=SHA256(M
1
	​

∣∣T
1
	​

∣∣H
0
	​

)
𝐻
2
=
𝑆
𝐻
𝐴
256
(
𝑀
2
∣
∣
𝑇
2
∣
∣
𝐻
1
)
H
2
	​

=SHA256(M
2
	​

∣∣T
2
	​

∣∣H
1
	​

)

Thus we obtain:

Log0 → H0
Log1 → H1
Log2 → H2
Log3 → H3

Each log entry depends on the previous hash, forming a chain.

7️⃣ Tampering Detection Mechanism

If an attacker modifies a message:

Original
UserB: Hi

to

Tampered
UserB: Send OTP

The recalculated hash becomes:

𝐻
𝑖
′
≠
𝐻
𝑖
H
i
′
	​


=H
i
	​


This causes:

Hash mismatch

which breaks the entire chain.

The system then reports:

Tampering Detected
8️⃣ Application Workflow
Step 1 — User Sends Message
UserA: Hello
Step 2 — Log Entry Created
Message: UserA: Hello
Timestamp: t1
PrevHash: H0
Hash: H1
Step 3 — New Log Added to Chain
Log0 → Log1 → Log2
Step 4 — Admin Verifies Chain

The system recomputes all hashes.

If:

Stored Hash = Recomputed Hash

Logs are valid.

Otherwise:

Tampering Detected
9️⃣ Installation and Setup
Step 1 — Clone the Repository
git clone https://github.com/yourusername/tamper-proof-chat-streamlit.git
Step 2 — Navigate to Project Directory
cd tamper-proof-chat-streamlit
Step 3 — Install Dependencies
pip install -r requirements.txt

or manually:

pip install streamlit
🔟 Running the Project

Run the Streamlit application:

streamlit run app.py
Open in Browser
http://localhost:8501
1️⃣1️⃣ Demonstration Scenario
Step 1 — Users Send Messages
UserA: Hello
UserB: Hi
Step 2 — Admin Opens Log Panel

Status:

Logs are VALID
Step 3 — Admin Simulates Tampering

Example modification:

UserB: Send OTP
Step 4 — System Verification

Result:

Tampering Detected
1️⃣2️⃣ Real-World Applications

Hash-chained logging is used in:

Blockchain Systems

Ensures immutability of transactions.

Financial Systems

Protects banking transaction logs.

Security Monitoring

Prevents attackers from hiding traces.

Digital Forensics

Maintains trustworthy evidence records.

Audit Trails

Ensures regulatory compliance.

1️⃣3️⃣ Future Improvements

Potential enhancements include:

Real-time multi-user chat using WebSockets

Digital signatures for log authentication

Distributed logging using blockchain

Database storage instead of JSON

Automated intrusion alerts

Visualization of hash chains

👨‍💻 Technologies Used

Python

Streamlit

SHA-256 Hashing

JSON Storage

📜 License

This project is provided for educational and research purposes.
