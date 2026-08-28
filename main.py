import time
import os
import sys
import argparse
import processPackets

def display_banner(skip_delay=False):
    banner = r"""
  ┌───────────────────────────────────────────────────────┐
  │          Network Intrusion Prevention System          │
  ├───────────────────────────────────────────────────────┤
  │   Developed by  :  Krishnamoorthi P L                 │
  │   Purpose       :  Detects and mitigates network      │
  │                    intrusions in real-time.           │
  │                                                       │
  │   Features      : - Rule-based detection              │
  │                   - Dynamic Filtering                 │
  │                   - Enhanced logging mechanism        │
  │   Note          :  Designed for learning and          │
  │                    experimentation in cybersecurity.  │
  └───────────────────────────────────────────────────────┘
"""
    print(banner)
    if not skip_delay:
        time.sleep(1.5)
    print("Network IPS rule engine started monitoring...\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Network Intrusion Prevention System (NIPS)")
    parser.add_argument("--no-banner", action="store_true", help="Skip banner display delay")
    parser.add_argument("-r", "--rules", default="customRules.txt", help="Path to rules file")
    args = parser.parse_args()

    display_banner(skip_delay=args.no_banner)
    processPackets.processpackets.StartQueueing()
