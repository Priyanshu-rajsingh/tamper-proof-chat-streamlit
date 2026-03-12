import streamlit as st
import logchain

st.title("Secure Chat with Tamper-Proof Logging")

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

    st.header("Chat System")

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

    st.header("Admin Log Monitor")

    status = logchain.verify_logs()

    if status:
        st.success("Logs are VALID")
    else:
        st.error("Tampering Detected!")

    logs = logchain.load_logs()

    for i, log in enumerate(logs):

        with st.expander(f"Log Entry {i+1}"):

            st.write("Message:", log["message"])
            st.write("Timestamp:", log["timestamp"])
            st.write("Previous Hash:", log["prev_hash"])
            st.write("Hash:", log["hash"])

    st.divider()

    if st.button("Reset Logs"):
        logchain.clear_logs()
        st.success("Logs Reset")

    if st.button("Simulate Hacker Tampering"):
        logchain.simulate_tamper()
        st.warning("⚠️ Hacker Tampered With Logs!")
