# Cisco Nexus Exports

## Overview
The `cisco_nexus_exports.py` script automates the process of collecting configuration and version details from multiple Cisco Nexus switches. It reads a file containing IP addresses, executes the `show run` and `show version` commands on each switch, and exports the results to separate files per IP address.

## Features
- Reads a file of IP addresses for Cisco Nexus switches.
- Connects to each switch and runs:
  - `show run`
  - `show version`
- Saves output in individual files named per IP address.
- Requires a single interactive login, used for all devices.
- Implements exception handling for connection and execution errors.

## Requirements
Ensure you have the following Python modules installed:
- `netmiko`
- `paramiko`
- `getpass`
- `tkinter`

## Installation
Install the required modules using pip:
```sh
pip install netmiko paramiko
```

## Usage
1. Run the script and select the file containing the switch IP addresses using the file dialog.
   ```sh
   python cisco_nexus_exports.py
   ```
2. Enter login credentials when prompted.
3. The script will connect to each switch and export outputs into individual files.

## Exception Handling
- Handles incorrect credentials.
- Manages connection timeouts and unreachable devices.
- Ensures file operations do not fail due to permission issues.

## License
This project is licensed under the MIT License.

## Contribution
Contributions are welcome! Feel free to fork and submit pull requests.

## Author
[Your Name]

