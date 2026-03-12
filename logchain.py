import hashlib
import json
import time

LOG_FILE = "logs.json"


def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()


def load_logs():
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_logs(logs):
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)


def add_log(message):

    logs = load_logs()

    prev_hash = logs[-1]["hash"] if logs else "0"

    timestamp = str(time.time())

    data = message + timestamp + prev_hash

    current_hash = calculate_hash(data)

    log_entry = {
        "message": message,
        "timestamp": timestamp,
        "prev_hash": prev_hash,
        "hash": current_hash
    }

    logs.append(log_entry)

    save_logs(logs)


def verify_logs():

    logs = load_logs()

    for i in range(len(logs)):

        prev_hash = logs[i]["prev_hash"]

        if i == 0:
            expected_prev = "0"
        else:
            expected_prev = logs[i-1]["hash"]

        data = logs[i]["message"] + logs[i]["timestamp"] + prev_hash

        recalculated_hash = calculate_hash(data)

        if prev_hash != expected_prev:
            return False

        if logs[i]["hash"] != recalculated_hash:
            return False

    return True


def clear_logs():
    with open(LOG_FILE, "w") as f:
        json.dump([], f)


def simulate_tamper():

    logs = load_logs()

    if len(logs) > 0:

        logs[0]["message"] = "⚠️ HACKED MESSAGE"

        save_logs(logs)
