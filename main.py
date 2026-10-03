import re 

with open("/var/log/auth.log", "r") as file:
    for line in file:

        # Extract username
        match = re.search(r"user\s+'([^']+)'", line)

        if not match:
            match = re.search(r"user=([^\s(]+)", line)

        if not match:
            match = re.search(r"user\s+([^\s(']+)", line)

        if match:
            username = match.group(1)
            print("Username:", username)

        # Extract PID
        pid_match = re.search(r"\[(\d+)\]", line)

        if pid_match:
            pid = pid_match.group(1)
            print("PID:", pid)

        # Extract IP
        ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)" , line)

        if ip_match:
           ip = ip_match.group(1)
           print("IP Address:", ip)

        # Extract Timestamp
        timestamp_match = re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}:\d{2}", line)

        if timestamp_match:
           timestamp = timestamp_match.group()
           print("Timestamp:", timestamp)
