# Auth Log Parser

A command-line utility for parsing and analyzing Linux authentication logs.

The tool reads authentication log files, extracts useful security-related information, identifies different authentication and session events, and 
generates summary statistics.

## Features

- Parse Linux authentication log files
- Extract timestamps
- Extract usernames
- Extract process IDs (PIDs)
- Extract source IP addresses
- Extract port numbers
- Identify authentication and session events
- Identify authentication failures
- Count different event types
- Count authentication successes and failures
- Display top usernames
- Display top source IP addresses
- Support custom log file paths using the `--file` command-line option
- Ignore malformed or unrecognized log lines

## Usage

Run the parser by providing the path to an authentication log file:

```bash
python3 main.py --file /path/to/auth.log
```
For example:

```bash
python3 main.py --file /var/log/auth.log.1
```

To view the available command-line options:

```bash
python3 main.py --help
```

## How It Works

The parser follows these basic steps:

1. Reads the authentication log file line by line.
2. Identifies relevant authentication and session events.
3. Uses regular expressions to extract information such as timestamps, usernames, PIDs, IP addresses, and ports.
4. Stores the extracted information in dictionaries.
5. Stores all recognized records in a list.
6. Calculates summary statistics from the parsed records.
7. Displays the results in the terminal.

## Requirements

1. Python 3
2. Linux authentication log file
3. Python standard library

No external Python packages are required.

## Project Structure

auth-log-parser/
├── main.py
├── README.md
└── .gitignore

## Example Output

```text
File path: /var/log/auth.log.1
Total records: 261

Event Summary:
Session Open : 130
Session Close : 84
Sudo Command : 41
Authentication Failure : 6

Status Summary:
Failure : 6

Top usernames:
root : 137
gdm-greeter : 49
harshstayswithastick : 34

Top IPs:
No IP addresses found.

Authentication Summary:

Successful authentications: 0
Failed authentications: 6
```

## Technologies Used

1. Python
2. Regular Expressions
3. argparse
4. Git
5. GitHub
