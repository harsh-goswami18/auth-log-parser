import re 
import argparse

records = []

parser = argparse.ArgumentParser(description="Auth Log Parser")

parser.add_argument("--file", required=True, help="Path to the authentication log file")

args = parser.parse_args()
print("File path:", args.file)

with open(args.file, "r") as file:
    for line in file:

        username = ""
        pid = ""
        ip = ""
        timestamp = ""
        event = ""
        status = ""
        port = ""


        # Extract username
        match = re.search(r"user=([^\s]+)", line)

        if not match:
            match = re.search(r"session opened for user\s+([^\s(]+)", line)

        if not match:
            match = re.search(r"session closed for user\s+([^\s]+)", line)

        if not match:
            match = re.search(r"of user\s+'([^']+)'", line)

        if match:
            username = match.group(1)

        # Extract PID
        pid_match = re.search(r"\[(\d+)\]", line)

        if pid_match:
            pid = pid_match.group(1)

        # Extract IP
        ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)" , line)

        if ip_match:
           ip = ip_match.group(1)

        # Extract Port
        port_match = re.search(r"port (\d+)", line)

        if port_match:
           port = port_match.group(1)

        # Extract Timestamp
        timestamp_match = re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}:\d{2}", line)

        if timestamp_match:
           timestamp = timestamp_match.group()

        # Detect Event Type
        if "authentication failure" in line:
            event = "Authentication Failure"

        if "session opened" in line:
            event = "Session Open"

        if "session closed" in line:
            event = "Session Close"

        if "COMMAND=" in line:
            event = "Sudo Command"

        # Detect SSH Authentication
        if "sshd" in line:
            if "Accepted" in line:
                event = "SSH Authentication"

            if "Failed password" in line:
                event = "SSH Authentication"

            if "Invalid user" in line:
                event = "SSH Authentication"

          # Detect Status
        if "authentication failure" in line:
            status = "Failure"

        elif "sshd" in line and "Failed password" in line:
            status = "Failure"

        elif "sshd" in line and "Invalid user" in line:
            status = "Failure"

        elif "sshd" in line and "Accepted" in line:
            status = "Success"

        record = {
            "Timestamp": timestamp,
            "Username": username,
            "IP": ip,
            "PID": pid,
            "Event": event,
            "Status": status,
            "Port": port
        }

        if event:
            records.append(record)

print("Total records:", len(records))
event_counts = {}

for record in records:
    event = record["Event"]

    if event not in event_counts:
        event_counts[event] = 0

    event_counts[event] += 1

print("Event Summary:")

for event, count in event_counts.items():
    print(event, ":", count)

status_counts = {}

for record in records:
    status = record["Status"]

    if status not in status_counts:
        status_counts[status] = 0

    status_counts[status] += 1

print("Status Summary:")

for status, count in status_counts.items():
    if status:
        print(status, ":", count)

username_counts = {}

for record in records:
    username = record["Username"]

    if username:
        if username not in username_counts:
            username_counts[username] = 0

        username_counts[username] += 1

sorted_users = sorted(
    username_counts.items(),
    key=lambda item: item[1],
    reverse=True
)

print("Top usernames:")

for username, count in sorted_users:
    print(username, ":", count)

ip_counts = {}

for record in records:
    ip = record["IP"]

    if ip:
        if ip not in ip_counts:
            ip_counts[ip] = 0

        ip_counts[ip] += 1

sorted_ip = sorted(ip_counts.items(),key=lambda item: item[1], reverse=True)
print("Top IPs:")

if sorted_ip:
    for ip, count in sorted_ip:
        print(ip, ":", count)
else:
    print("No IP addresses found.")

success_count = 0
failure_count = 0

for record in records:
    if record["Status"] == "Success":
        success_count += 1

    elif record["Status"] == "Failure":
        failure_count += 1

print("Authentication Summary:")
print("Successful authentications:", success_count)
print("Failed authentications:", failure_count)
