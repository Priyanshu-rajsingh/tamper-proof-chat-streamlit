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

    st.subheader("View Logs")

    for i, log in enumerate(logs):

        with st.expander(f"Log Entry {i}"):

            st.write("Message:", log["message"])
            st.write("Timestamp:", log["timestamp"])
            st.write("Previous Hash:", log["prev_hash"])
            st.write("Hash:", log["hash"])

    st.divider()

    st.subheader("Simulate Log Tampering")

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
