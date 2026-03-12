import streamlit as st
import logchain

st.set_page_config(page_title="Tamper Proof Chat", layout="wide")

st.title("🔐 Secure Chat with Tamper-Proof Logging")

st.sidebar.title("Navigation")

user = st.sidebar.selectbox(
    "Select User",
    ["UserA", "UserB"]
)

page = st.sidebar.selectbox(
    "Page",
    ["Chat", "Admin Panel"]
)

# ---------------- CHAT PAGE ----------------

if page == "Chat":

    st.header("💬 Chat System")

    message = st.text_input("Enter message")

    if st.button("Send Message"):

        if message:
            logchain.add_log(f"{user}: {message}")
            st.success("Message sent")

    st.subheader("Chat History")

    logs = logchain.load_logs()

    for log in logs:
        st.write(log["message"])


# ---------------- ADMIN PANEL ----------------

if page == "Admin Panel":

    st.header("🛠 Admin Log Monitor")

    logs = logchain.load_logs()

    status = logchain.verify_logs()

    if status:
        st.success("Logs are VALID")
    else:
        st.error("⚠ Tampering Detected!")

    st.divider()

    st.subheader("📜 Logs")

    for i, log in enumerate(logs):

        with st.expander(f"Log Entry {i}"):

            st.write("Message:", log["message"])
            st.write("Timestamp:", log["timestamp"])
            st.write("Previous Hash:", log["prev_hash"])
            st.write("Hash:", log["hash"])

    st.divider()

    st.subheader("⚠ Simulate Log Tampering")

    if len(logs) > 0:

        tamper_index = st.number_input(
            "Select Log Index",
            min_value=0,
            max_value=len(logs)-1,
            step=1
        )

        new_message = st.text_input("Enter Tampered Message")

        if st.button("Tamper Log"):

            logchain.tamper_log(int(tamper_index), new_message)

            st.warning("Log has been tampered!")

    st.divider()

    if st.button("Reset Logs"):
        logchain.clear_logs()
        st.success("Logs Reset")

    st.divider()

    # ---------------- VISUAL HASH CHAIN ----------------

    st.subheader("🔗 Hash Chain Visualization")

    logs = logchain.load_logs()

    valid_chain = logchain.verify_logs()

    if len(logs) > 0:

        cols = st.columns(len(logs))

        for i, log in enumerate(logs):

            with cols[i]:

                if valid_chain:
                    color = "#28a745"
                else:
                    color = "#dc3545"

                st.markdown(
                    f"""
                    <div style="
                        border:2px solid {color};
                        border-radius:10px;
                        padding:15px;
                        text-align:center;
                        background-color:#111;
                        color:white;
                    ">
                    <b>Log {i}</b><br><br>
                    {log["message"]}<br><br>
                    <small>Hash:</small><br>
                    <code>{log["hash"][:12]}...</code>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    st.divider()

    st.subheader("🔄 Hash Chain Flow")

    if len(logs) > 0:

        chain_text = ""

        for i in range(len(logs)):
            chain_text += f"[Log{i}] → "

        chain_text += "END"

        st.code(chain_text)

    st.divider()

    st.subheader("📖 How Tamper-Proof Logging Works")

    st.markdown("""
    ### Step 1
    Each chat message is stored as a log entry.
    
    Example:
    
    UserA: Hello  
    UserB: Hi  
    
    Each message becomes a **log record**.
    
    ---
    
    ### Step 2
    Each log stores the **hash of the previous log**.
    
    This creates a dependency between logs.
    
    
    Log0 → Hash0
    Log1 → Hash(Hash0 + Log1)
    Log2 → Hash(Hash1 + Log2)
    
    
    ---
    
    ### Step 3
    The hash is calculated using the SHA-256 algorithm.
    
    Example formula:
    
    
    Hash_i = SHA256(Message_i + Timestamp + Hash_(i-1))
    
    
    Because each log contains the previous hash, they form a **secure chain**.
    
    ---
    
    ### Step 4
    This creates a **tamper-proof structure**.
    
    
    [Log0] → [Log1] → [Log2] → [Log3]
    
    
    Each block depends on the previous block.
    
    ---
    
    ### Step 5
    If an attacker modifies a message:
    
    Example tampering:
    
    
    Original:
    UserB: Hi
    
    Tampered:
    UserB: Send OTP
    
    
    The stored hash will no longer match the recalculated hash.
    
    ---
    
    ### Step 6
    When the system verifies the logs:
    
    
    Recomputed Hash ≠ Stored Hash
    
    
    This indicates **tampering has occurred**.
    
    ---
    
    ### Step 7
    The system alerts the admin and marks the chain as **invalid**.
    
    This is how the system detects **log manipulation attacks**.
    
    ---
    
    ### Real-World Applications
    
    This technique is used in:
    
    • Blockchain systems  
    • Secure audit logs  
    • Financial transaction records  
    • Digital forensics  
    • Cybersecurity monitoring systems
    
    """)
