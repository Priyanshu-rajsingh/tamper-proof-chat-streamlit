import streamlit as st
import logchain

st.title("Secure Chat with Tamper-Proof Logging")

st.sidebar.title("User Settings")

user = st.sidebar.selectbox(
    "Select User",
    ["UserA", "UserB"]
)

page = st.sidebar.selectbox(
    "Page",
    ["Chat", "Admin Panel"]
)


# CHAT PAGE
if page == "Chat":

    st.header("Chat")

    message = st.text_input("Enter message")

    if st.button("Send"):

        if message:
            logchain.add_log(f"{user}: {message}")
            st.success("Message sent")

    st.subheader("Chat History")

    logs = logchain.load_logs()

    for log in logs:
        st.write(log["message"])


# ADMIN PANEL
if page == "Admin Panel":

    st.header("Admin Log Monitor")

    status = logchain.verify_logs()

    if status:
        st.success("Logs are VALID")
    else:
        st.error("Tampering Detected")

    logs = logchain.load_logs()

    for log in logs:

        with st.expander("Log Entry"):

            st.write("Message:", log["message"])
            st.write("Timestamp:", log["timestamp"])
            st.write("Previous Hash:", log["prev_hash"])
            st.write("Hash:", log["hash"])

    if st.button("Reset Logs"):
        logchain.clear_logs()
        st.success("Logs cleared")