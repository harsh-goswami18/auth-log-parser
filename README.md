# Auth Log Parser

An auth log parser is a program that reads raw Linux or system authentication log files (auth.log) and converts unstructured texts into structured
and useful data.

The tool parses authentication log files and identifies different authentication and session events, and generates useful security related
information and summary statistics.

It also includes brute-force attack detection and an option to export the parsed records into a CSV file.

## Features

- Parse Linux authentication log files
- Extract timestamps
- Extract usernames
- Extract process IDs (PIDs)
- Extract source IP addresses
- Extract port numbers
- Identify different authentication and session events
- Identify successfull or failed authentication attempts
- Count different event types
- Count authentication successes and failures
- Display top usernames
- Display top IP addresses
- Support custom log file paths using the `--file` command-line option
- Detect Brute-Force attacks
- Export output in CSV format

## Technologies Used

1. Python
2. Linux
3. Regular Expressions
4. argparse
5. csv
6. datetime
7. Git
8. GitHub

## Requirements

1. Python
2. Linux authentication log file
3. Python standard libraries

## Usage

Run the parser by providing the path of an authentication log file:

python3 main.py --file /path/to/auth.log

For example:

python3 main.py --file /var/log/auth.log.1

## How It Works

The parser follows these steps:

1. Reads the authentication log file line by line
2. Identifies useful authentication and session events
3. Uses regular expressions to extract information such as timestamps, usernames, PIDs, IP addresses, and ports
4. Stores the extracted information in dictionaries
5. Stores all recognized records in a list
6. Calculates summary statistics from the parsed records
7. Displays the results in the terminal
8. Checks failed authentication attempts to detect brute-force attacks
9. Allows the parsed records to be exported to a CSV file when asked

## CSV EXPORT 

The parsed records can also be exported to a CSV file.

Command:

python3 main.py --file /path/to/auth.log --csv output.csv

The CSV file contains columns such as:

- Timestamp
- Username
- IP
- PID
- Event
- Status
- Port

## Brute-Force Detection

The program also checks failed authentication attempts from a same IP address.

If 5 failed attempts occur within 300 seconds, the program alerts a possible brute-force attack.

Example:

Possible brute-force attack detected!
IP: 10.0.0.15
Failed attempts: 5
Time period: 240.0 seconds

## Error Handling

If the input log file does not exist, the program displays an error message.

Example:

Error: File not found: filename.log

## Example Output

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
CSV file created: output.csv

## Author

Harsh Goswami
B.Tech IT
Delhi Technological University
is this good? and doesnt look like ai generated
