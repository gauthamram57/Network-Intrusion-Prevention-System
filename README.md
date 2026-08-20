# Network Intrusion Prevention System (NIPS)

A real-time Network Intrusion Prevention System (NIPS) built with Python, Scapy, NetfilterQueue, and `iptables`. Features packet inspection, custom signature-based rule matching, automated threat mitigation (packet dropping & IP blocking), and attack event logging.

## 🚀 Features

- **Real-Time Packet Inspection**: Intercepts network packets live using `NetfilterQueue` and `Scapy`.
- **Custom Signature Rules**: Implements rule matching for SYN floods, ICMP/UDP floods, SQL Injection, XSS, and directory traversal.
- **Automated Mitigation**: Automatically drops malicious packets and inserts `iptables` drop rules to block attacking IPs.
- **Structured Security Logging**: Exports detailed attack logs (`attackLogs.csv`) and analyzed traffic records (`trafficLogs.csv`).

## 📁 Project Structure

```
Network-Intrusion-Prevention-System/
├── main.py                # Core entry point and NetfilterQueue loop
├── processPackets.py      # Extracts IP, TCP, UDP, and payload attributes
├── matchRules.py          # Signature matching engine against custom rules
├── doActions.py            # Executes mitigation (packet drop & firewall rules)
├── storeLogs.py           # Ingestion & CSV logging utility
├── customRules.txt        # Signature rule definition file
├── attackLogs.csv         # Log storage for flagged attack events
├── trafficLogs.csv        # Log storage for processed traffic
├── LICENSE                # Open source license
└── README.md              # Documentation
```

## 🛠️ Installation & Setup

### Prerequisites

```bash
sudo apt update
sudo apt install iptables python3-pip
pip install scapy NetfilterQueue
```

### Running the NIPS Engine

```bash
# Clone repository
git clone https://github.com/gauthamram57/Network-Intrusion-Prevention-System.git
cd Network-Intrusion-Prevention-System

# Run NIPS engine with root privileges
sudo python3 main.py
```

## 📜 License

This project is licensed under the [MIT License](LICENSE).
